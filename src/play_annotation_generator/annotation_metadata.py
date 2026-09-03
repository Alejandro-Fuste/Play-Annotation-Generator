import csv
import json
import os
from typing import Any, Dict, List, Optional, Tuple, Set


def parse_dataset_timestamp(val: Optional[str]) -> Tuple[Optional[float], Optional[str]]:
    """
    Parses a timestamp string like '0:00:02', '0:02:35', or '1:04:40' to float seconds.
    Returns (seconds_float_or_none, warning_msg_or_none).
    """
    if val is None:
        return None, None
    val_str = str(val).strip()
    if not val_str:
        return None, None

    parts = val_str.split(":")
    if not (1 <= len(parts) <= 3):
        return None, f"Metadata: invalid timestamp format '{val_str}'"

    try:
        if len(parts) == 1:
            sec = float(parts[0])
        elif len(parts) == 2:
            sec = float(parts[0]) * 60.0 + float(parts[1])
        else:  # 3 parts: H:MM:SS
            sec = float(parts[0]) * 3600.0 + float(parts[1]) * 60.0 + float(parts[2])
        return sec, None
    except ValueError:
        return None, f"Metadata: invalid numeric timestamp value '{val_str}'"


def parse_from_youtube(val: Optional[str]) -> Tuple[Optional[bool], Optional[str]]:
    """
    Normalizes 'fromYouTube' boolean column.
    TRUE / true / 1 -> True
    FALSE / false / 0 -> False
    blank -> None
    unexpected -> None + warning
    """
    if val is None:
        return None, None
    v = str(val).strip()
    if not v:
        return None, None
    v_upper = v.upper()
    if v_upper in ("TRUE", "1", "YES"):
        return True, None
    elif v_upper in ("FALSE", "0", "NO"):
        return False, None
    else:
        return None, f"Metadata: invalid fromYouTube boolean value '{v}'"


def load_dataset_summary(summary_csv_path: str) -> Tuple[Dict[str, List[Dict[str, str]]], Optional[str]]:
    """
    Loads Dataset Summary.csv and builds an index mapping normalized output_file -> list of row dicts.
    Returns (index, error_message_if_file_missing).
    """
    if not summary_csv_path or not os.path.exists(summary_csv_path):
        # Check space vs non-space candidate
        alt_path = None
        if "Dataset Summary.csv" in summary_csv_path:
            alt_path = summary_csv_path.replace("Dataset Summary.csv", "DatasetSummary.csv")
        elif "DatasetSummary.csv" in summary_csv_path:
            alt_path = summary_csv_path.replace("DatasetSummary.csv", "Dataset Summary.csv")

        if alt_path and os.path.exists(alt_path):
            summary_csv_path = alt_path
        else:
            return {}, f"Metadata catalog: required file not found: {summary_csv_path}"

    index: Dict[str, List[Dict[str, str]]] = {}
    with open(summary_csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            out_file = (row.get("output_file") or "").strip()
            if out_file:
                norm_key = os.path.basename(out_file).lower()
                index.setdefault(norm_key, []).append(row)

    return index, None


def resolve_clip_source_metadata(
    dataset_summary_index: Dict[str, List[Dict[str, str]]],
    video_name: str
) -> Tuple[Dict[str, Any], List[str], List[str]]:
    """
    Resolves clip-source metadata for target video_name.
    Returns (clip_source_dict, warnings_list, errors_list).
    """
    warnings: List[str] = []
    errors: List[str] = []

    null_source = {
        "start_time": None,
        "end_time": None,
        "clip_length": None,
        "time_unit": "seconds",
        "view": None,
        "from_youtube": None
    }

    if not video_name:
        return null_source, warnings, errors

    clean_name = os.path.basename(video_name.strip())
    candidates = [clean_name.lower()]

    # If target video_name does not end with .mp4, add .mp4 candidate
    if not clean_name.lower().endswith(".mp4"):
        candidates.append(f"{clean_name.lower()}.mp4")

    matched_rows: List[Dict[str, str]] = []
    matched_key = None

    for cand in candidates:
        if cand in dataset_summary_index:
            matched_rows = dataset_summary_index[cand]
            matched_key = cand
            break

    if not matched_rows:
        warnings.append(f"Metadata: no Dataset Summary row found for output_file '{clean_name}'; source metadata written as null.")
        return null_source, warnings, errors

    if len(matched_rows) > 1:
        errors.append(f"Metadata: multiple Dataset Summary rows found for output_file '{matched_key}'; clip source metadata is ambiguous.")
        return null_source, warnings, errors

    row = matched_rows[0]

    raw_start = row.get("start_time")
    raw_end = row.get("end_time")
    raw_view = row.get("view")
    raw_youtube = row.get("fromYouTube")

    start_sec, w_start = parse_dataset_timestamp(raw_start)
    if w_start:
        warnings.append(w_start)

    end_sec, w_end = parse_dataset_timestamp(raw_end)
    if w_end:
        warnings.append(w_end)

    clip_length = None
    if start_sec is not None and end_sec is not None:
        if end_sec >= start_sec:
            clip_length = round(end_sec - start_sec, 3)
        else:
            errors.append(f"Metadata: end_time precedes start_time for '{clean_name}'.")

    view_val = raw_view.strip() if raw_view and raw_view.strip() else None

    from_yt_val, w_yt = parse_from_youtube(raw_youtube)
    if w_yt:
        warnings.append(w_yt)

    resolved_source = {
        "start_time": start_sec,
        "end_time": end_sec,
        "clip_length": clip_length,
        "time_unit": "seconds",
        "view": view_val,
        "from_youtube": from_yt_val
    }

    return resolved_source, warnings, errors


def load_action_definitions(actions_json_path: str) -> Tuple[Dict[str, str], Dict[str, Dict[str, Any]], Optional[str]]:
    """
    Loads actions11.json.
    Returns (canonical_to_human_dict, action_definitions_raw_dict, error_message_if_failed).
    """
    if not actions_json_path or not os.path.exists(actions_json_path):
        return {}, {}, f"Metadata catalog: required file not found: {actions_json_path}"

    try:
        with open(actions_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return {}, {}, f"Metadata catalog: failed to parse JSON from {actions_json_path}: {e}"

    formatted_labels = data.get("formattedActionLabels")
    action_labels = data.get("actionLabels")
    action_defs = data.get("actionDefinitions")

    if not isinstance(formatted_labels, list) or not isinstance(action_labels, list):
        return {}, {}, f"Metadata catalog: actions11.json formattedActionLabels or actionLabels is not a list."

    if len(formatted_labels) != len(action_labels):
        return {}, {}, f"Metadata catalog: actions11.json formattedActionLabels/actionLabels lengths differ."

    if not isinstance(action_defs, dict):
        return {}, {}, f"Metadata catalog: actions11.json actionDefinitions is not an object."

    canonical_to_human: Dict[str, str] = {}
    for i in range(len(formatted_labels)):
        c_label = str(formatted_labels[i]).strip()
        h_label = str(action_labels[i]).strip()
        canonical_to_human[c_label] = h_label

    return canonical_to_human, action_defs, None


def resolve_used_action_definitions(
    segments: List[Dict[str, Any]],
    canonical_to_human: Dict[str, str],
    action_defs_raw: Dict[str, Dict[str, Any]]
) -> Tuple[Dict[str, Dict[str, Optional[str]]], List[str]]:
    """
    Resolves definitions for actions used in action segments.
    Returns (resolved_actions_dict_sorted, warnings_list).
    """
    warnings: List[str] = []
    used_canonical_actions: Set[str] = set()

    for seg in segments:
        act = seg.get("action")
        if act and isinstance(act, str):
            used_canonical_actions.add(act.strip())

    resolved_defs: Dict[str, Dict[str, Optional[str]]] = {}

    for canonical_act in sorted(used_canonical_actions):
        human_label = canonical_to_human.get(canonical_act)
        matched_entry = None
        label_out = None

        if human_label and human_label in action_defs_raw:
            matched_entry = action_defs_raw[human_label]
            label_out = human_label
        elif canonical_act in action_defs_raw:
            matched_entry = action_defs_raw[canonical_act]
            label_out = canonical_act

        def_text = None
        if matched_entry and isinstance(matched_entry, dict):
            def_text = matched_entry.get("definition")

        if def_text is None and matched_entry is None:
            warnings.append(f"Action definition: no definition found for '{canonical_act}'.")
            resolved_defs[canonical_act] = {
                "label": None,
                "definition": None
            }
        else:
            resolved_defs[canonical_act] = {
                "label": label_out,
                "definition": def_text
            }

    return resolved_defs, warnings


def load_play_definitions(plays_json_path: str) -> Tuple[Dict[str, str], Dict[str, Dict[str, Any]], Optional[str]]:
    """
    Loads plays.json.
    Supports 'defintions' and fallback 'definitions'.
    Returns (canonical_play_to_lookup_dict, play_defs_raw_dict, error_message_if_failed).
    """
    if not plays_json_path or not os.path.exists(plays_json_path):
        return {}, {}, f"Metadata catalog: required file not found: {plays_json_path}"

    try:
        with open(plays_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return {}, {}, f"Metadata catalog: failed to parse JSON from {plays_json_path}: {e}"

    formatted_plays = data.get("formattedPlayLabels")
    play_labels = data.get("playLabels")
    play_defs = data.get("defintions")
    if play_defs is None:
        play_defs = data.get("definitions")

    if not isinstance(formatted_plays, list) or not isinstance(play_labels, list):
        return {}, {}, f"Metadata catalog: plays.json formattedPlayLabels or playLabels is not a list."

    if not isinstance(play_defs, dict):
        return {}, {}, f"Metadata catalog: plays.json defintions/definitions is not an object."

    canonical_to_lookup: Dict[str, str] = {}
    min_len = min(len(formatted_plays), len(play_labels))
    for i in range(min_len):
        c_play = str(formatted_plays[i]).strip()
        h_play = str(play_labels[i]).strip()
        canonical_to_lookup[c_play] = h_play

    return canonical_to_lookup, play_defs, None


def resolve_play_definition(
    play_tag: Optional[str],
    canonical_to_lookup: Dict[str, str],
    play_defs_raw: Dict[str, Dict[str, Any]]
) -> Tuple[Optional[str], List[str]]:
    """
    Resolves textual definition for a play tag.
    Returns (definition_str_or_none, warnings_list).
    """
    warnings: List[str] = []
    if not play_tag:
        return None, warnings

    clean_tag = play_tag.strip()
    lookup_label = canonical_to_lookup.get(clean_tag)

    matched_entry = None
    if lookup_label and lookup_label in play_defs_raw:
        matched_entry = play_defs_raw[lookup_label]
    elif clean_tag in play_defs_raw:
        matched_entry = play_defs_raw[clean_tag]

    def_text = None
    if matched_entry and isinstance(matched_entry, dict):
        def_text = matched_entry.get("definition")

    if def_text is None:
        warnings.append(f"Play definition: no definition found for '{clean_tag}'.")
        return None, warnings

    return def_text, warnings
