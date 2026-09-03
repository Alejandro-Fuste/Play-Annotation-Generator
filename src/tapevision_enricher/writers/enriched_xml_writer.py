import xml.etree.ElementTree as ET
from typing import Any, Dict, List
from ..models import ActionSegment, Track

def write_enriched_xml(
    input_xml_path: str,
    output_xml_path: str,
    segments: List[ActionSegment],
    tracks: Dict[str, Track],
    config: Dict[str, Any],
    metadata: Optional[Dict[str, Any]] = None
) -> None:
    """
    Reads the original XML and writes a new enriched XML.
    Adds box-level action attributes for player tracks inside active action segments.
    Injects or updates the <tapevision> metadata block under <meta>.
    """
    tree = ET.parse(input_xml_path)
    root = tree.getroot()
    
    player_lbl = config.get("labels", {}).get("player_label", "player")
    policy_cfg = config.get("action_policy", {})
    default_offense_act = policy_cfg.get("default_unlabeled_offense_action", "Action_Unknown")
    default_defense_act = policy_cfg.get("default_unlabeled_defense_action", "Action_Defense_NotAnnotated")
    
    # 1. Inject or update <tapevision> block under <meta>
    meta_elem = root.find("meta")
    if meta_elem is None:
        meta_elem = ET.SubElement(root, "meta")

    # Remove existing <tapevision> for idempotency
    existing_tv = meta_elem.find("tapevision")
    if existing_tv is not None:
        meta_elem.remove(existing_tv)

    if metadata:
        tv_elem = ET.SubElement(meta_elem, "tapevision")

        def _add_xml_field(parent: ET.Element, tag_name: str, val: Any, attribs: Optional[Dict[str, str]] = None) -> ET.Element:
            attr_dict = attribs.copy() if attribs else {}
            if val is None:
                attr_dict["null"] = "true"
                elem = ET.SubElement(parent, tag_name, attr_dict)
            else:
                elem = ET.SubElement(parent, tag_name, attr_dict)
                if isinstance(val, bool):
                    elem.text = "true" if val else "false"
                else:
                    elem.text = str(val)
            return elem

        # <clip_source>
        clip_src = metadata.get("clip_source", {})
        clip_elem = ET.SubElement(tv_elem, "clip_source")
        _add_xml_field(clip_elem, "start_time", clip_src.get("start_time"), {"unit": "seconds"})
        _add_xml_field(clip_elem, "end_time", clip_src.get("end_time"), {"unit": "seconds"})
        _add_xml_field(clip_elem, "clip_length", clip_src.get("clip_length"), {"unit": "seconds"})
        _add_xml_field(clip_elem, "view", clip_src.get("view"))
        _add_xml_field(clip_elem, "from_youtube", clip_src.get("from_youtube"))

        # <play>
        play_elem = ET.SubElement(tv_elem, "play")
        _add_xml_field(play_elem, "tag", metadata.get("play_tag"))
        _add_xml_field(play_elem, "definition", metadata.get("play_definition"))

        # <action_definitions>
        act_defs_elem = ET.SubElement(tv_elem, "action_definitions")
        act_defs_dict = metadata.get("action_definitions", {})

        for canonical_act, entry in act_defs_dict.items():
            lbl = entry.get("label")
            def_text = entry.get("definition")

            act_attribs = {"canonical": canonical_act}
            if lbl is not None:
                act_attribs["label"] = lbl
            if lbl is None and def_text is None:
                act_attribs["null"] = "true"

            act_node = ET.SubElement(act_defs_elem, "action", act_attribs)
            _add_xml_field(act_node, "definition", def_text)

        # <metadata_sources>
        sources_elem = ET.SubElement(tv_elem, "metadata_sources")
        meta_sources = metadata.get("metadata_sources", {})
        _add_xml_field(sources_elem, "dataset_summary", meta_sources.get("dataset_summary", "DatasetSummary.csv"))
        _add_xml_field(sources_elem, "actions", meta_sources.get("actions", "actions.json"))
        _add_xml_field(sources_elem, "plays", meta_sources.get("plays", "plays.json"))
    
    # 2. Pre-build segment lookup: xml_track_id -> list of ActionSegment
    segs_by_track: Dict[str, List[ActionSegment]] = {}
    for seg in segments:
        segs_by_track.setdefault(seg.xml_track_id, []).append(seg)
        
    for track_elem in root.findall("track"):
        xml_track_id = track_elem.attrib.get("id", "")
        label = track_elem.attrib.get("label", "")
        
        if label != player_lbl:
            continue
            
        # Retrieve parsed Track object to know position/team_side
        track = tracks.get(xml_track_id)
        if not track:
            continue
            
        is_offense = track.team_side == "offense"
        track_segs = segs_by_track.get(xml_track_id, [])
        
        for box_elem in track_elem.findall("box"):
            frame = int(box_elem.attrib.get("frame", "0"))
            
            # Find active segment for this frame
            active_seg = None
            for seg in track_segs:
                if seg.start_frame <= frame <= seg.end_frame:
                    active_seg = seg
                    break
                    
            if active_seg:
                action_label = active_seg.action
                action_source = active_seg.source if active_seg.source else "key_actions_csv_plus_temporal_rules"
                seg_start = str(active_seg.start_frame)
                seg_end = str(active_seg.end_frame)
            else:
                action_label = default_offense_act if is_offense else default_defense_act
                action_source = "default_policy"
                seg_start = ""
                seg_end = ""
                
            # Update attributes on box_elem
            target_attrs = {
                "tapevision_action": action_label,
                "tapevision_action_source": action_source,
                "tapevision_action_segment_start": seg_start,
                "tapevision_action_segment_end": seg_end
            }
            
            # Standard 'action' attribute check
            existing_action_elem = box_elem.find("./attribute[@name='action']")
            if existing_action_elem is not None:
                existing_action_elem.text = action_label
                
            # Add or update others
            for attr_name, attr_val in target_attrs.items():
                attr_elem = box_elem.find(f"./attribute[@name='{attr_name}']")
                if attr_elem is not None:
                    attr_elem.text = attr_val
                else:
                    new_attr = ET.Element("attribute", name=attr_name)
                    new_attr.text = attr_val
                    box_elem.append(new_attr)
                    
    # Format and save
    try:
        ET.indent(root, space="  ")
    except AttributeError:
        pass
        
    # Write to output file
    with open(output_xml_path, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
