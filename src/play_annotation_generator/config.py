import os
from typing import Any, Dict, Optional
import yaml

DEFAULT_CONFIG: Dict[str, Any] = {
    "input": {
        "cvat_xml": "",
        "action_csv": "",
        "gt_txt": "",
        "labels_txt": "",
        "xml_template": "",
        "key_actions_csv": "",
        "player_track_csv": "",
        "dataset_summary_csv": "data/DatasetSummary.csv",
        "actions_json": "data/actions.json",
        "plays_json": "data/plays.json"
    },
    "metadata_enrichment": {
        "enabled": True,
        "missing_source_file_policy": "error",
        "missing_clip_row_policy": "warning_null",
        "duplicate_clip_row_policy": "error",
        "missing_action_definition_policy": "warning_null",
        "missing_play_definition_policy": "warning_null"
    },
    "output": {
        "output_dir": "outputs/",
        "write_generated_base_xml": True,
        "write_enriched_xml": True,
        "write_play_annotation_json": True,
        "write_tapevision_json": True,
        "write_dense_csv": True,
        "write_validation_report": True,
        "write_review_report": True
    },
    "frame_indexing": {
        "mot_frame_index_base": 1,
        "cvat_frame_index_base": 0
    },
    "video": {
        "fps": 30,
        "width": 1920,
        "height": 1080,
        "video_length_frames_column": "video_length_frames"
    },
    "mot": {
        "class_id_to_label": {
            1: "player",
            2: "ball"
        },
        "default_label": "player"
    },
    "labels": {
        "player_label": "player",
        "ball_label": "ball"
    },
    "csv": {
        "format": "wide",
        "columns": {
            "video_name": "video_name",
            "video_id": "video_id",
            "play_tag": "play_tag",
            "result_tag": "result_tag",
            "result_frame": "result_frame",
            "notes": "notes"
        },
        "action_columns": {
            "pre_snap": "Action_PreSnap",
            "jet_motion": "Action_JetMotion",
            "ball_snap": "Action_BallSnap",
            "zone_block": "Action_ZoneBlock",
            "reach_block": "Action_ReachBlock",
            "down_block": "Action_DownBlock",
            "down_blocks": "Action_DownBlock",
            "pull_block": "Action_PullBlock",
            "pull_blocks": "Action_PullBlock",
            "pull_lead_block": "Action_PullLeadBlock",
            "combo_block": "Action_ComboBlock",
            "combo_blocks": "Action_ComboBlock",
            "split_block": "Action_SplitBlock",
            "crack_block": "Action_CrackBlock",
            "snap_receive": "Action_SnapReceive",
            "toss": "Action_Toss",
            "ball_carry": "Action_BallCarry",
            "seal_block": "Action_SealBlock",
            "lead_block": "Action_LeadBlock",
            "block_second_level": "Action_BlockSecondLevel",
            "run_block": "Action_RunBlock",
            "fake_handoff": "Action_FakeHandoff",
            "handoff": "Action_Handoff",
            "boot_away": "Action_BootAway",
            "run_flat_route": "Action_RunFlatRoute",
            "throw_pass": "Action_ThrowPass",
            "secure_catch": "Action_SecureCatch",
            "end_ol_block": "Action_None",
            "end_play": "Action_PlayEnd",
            "pass_block": "Action_PassBlock",
            "pass_drop": "Action_FakePassDroptoHandoff",
            "pump_fake": "Action_PumpFake",
            "clear_out_route": "Action_ClearToEdge",
            "dig_route": "Action_BreakInside",
            "run_deep_cross_route": "Action_RunDeepCrossRoute",
            "run_hitch_route": "Action_RunHitchRoute",
            "run_out_route": "Action_RunOutRoute",
            "run_post_route": "Action_RunPostRoute",
            "run_slant_route": "Action_RunSlantRoute",
            "sell_slant": "Action_SellRoute",
            "sell_out": "Action_SellOut",
            "run_go_route": "Action_VerticalStem",
            "release_to_screen": "Action_ReleaseToScreen",
            "turn_to_quarterback": "Action_TurnToQuarterback",
            "settle_for_screen": "Action_SettleForScreen",
            "throw_screen_pass": "Action_ThrowScreenPass",
            "screen_block": "Action_ScreenBlock",
            "run_after_catch": "Action_RunAfterCatch",
            "route": "Action_RunPostRoute",
            "read_defender": "Action_ReadDefender",
            "read_edge_defender": "Action_ReadEdgeDefender",
            "keep": "Action_Keep",
            "pull_ball": "Action_PullBall",
            "press_edge": "Action_PressEdge",
            "press_interior_gap": "Action_PressGap",
            "play_side_fake_step": "Action_PlaySideFakeStep",
            "kick_approach": "Action_KickApproach",
            "kick_ball": "Action_KickBall",
            "catch_kick": "Action_CatchKick",
            "cross_goal_line": "Action_CrossGoalLine",
            "onside_kick": "Action_KickBall",
            "attempt_recovery": "Action_AttemptRecovery",
            "secure_recovery": "Action_SecureRecovery",
            "long_snap": "Action_LongSnap",
            "place_ball": "Action_PlaceBall",
            "attempt_block": "Action_AttemptBlock",
            "block_kick": "Action_BlockKick",
            "punt_ball": "Action_PuntBall",
            "block_punt": "Action_BlockPunt",
            "catch_punt": "Action_CatchPunt",
            "tackle": "Action_Tackle",
            "close_on_quarterback": "Action_CloseOnQuarterback",
            "wrap_quarterback": "Action_WrapQuarterback",
            "sack_quarterback": "Action_SackQuarterback"
        },
        "cell_parsing": {
            "pair_separator": ",",
            "multi_entry_separators": [";", "|", "\n"],
            "allow_global_frame_only_events": True,
            "allow_position_group_targets": True
        }
    },
    "position_groups": {
        "OL": ["LT", "LG", "C", "RG", "RT"],
        "ALL_OFFENSE": ["QB", "RB", "FB", "H-BACK", "LT", "LG", "C", "RG", "RT", "WR-X", "WR-Y", "WR-Z", "WR-F", "TE-Y", "TE-H", "TE-F"],
        "SKILL": ["QB", "RB", "FB", "H-BACK", "WR-X", "WR-Y", "WR-Z", "WR-F", "TE-Y", "TE-H", "TE-F"]
    },
    "action_policy": {
        "default_unlabeled_player_action": "Action_None",
        "default_unlabeled_offense_action": "Action_None",
        "default_unlabeled_defense_action": "Action_None",
        "action_range_mode": "start_frame_only",
        "one_primary_action_per_frame": True,
        "missing_box_policy": "skip"
    },
    "play_end": {
        "source": "csv_result_or_end_of_play",
        "fallback": "final_xml_frame"
    },
    "validation": {
        "strict": False
    },
    "global_rules": {
        "one_primary_action_per_frame": True,
        "fill_uncovered_visible_frames_with": "Action_None",
        "default_unlabeled_player_action": "Action_None"
    },
    "pre_snap": {
        "applies_to": "ALL_MAPPED_PLAYERS",
        "start": "clip_start",
        "end": {
            "primary": "next_same_actor_explicit_action_minus_one",
            "fallback": "ball_snap_minus_one"
        }
    },
    "action_frame_semantics": {
        "Action_BallSnap": {
            "annotated_frame_role": "START",
            "end_from_action": "Action_SnapReceive",
            "event_type": "PRIMARY_ACTION"
        },
        "Action_SnapReceive": {
            "annotated_frame_role": "END",
            "start_from_action": "Action_BallSnap",
            "event_type": "PRIMARY_ACTION"
        }
    },
    "cross_actor_rules": {
        "Action_Toss": {
            "end_type": "next_action_of_type_minus_one",
            "target_action": "Action_BallCarry",
            "actor_scope": "any"
        }
    },
    "terminal_actions": {
        "Action_BallCarry": {
            "end_type": "final_clip_frame"
        }
    },
    "boundary_events": {
        "Action_None": {
            "event_type": "BOUNDARY",
            "applies_to_group": "OL",
            "source_column_alias": "end_ol_block",
            "inclusive_boundary": True,
            "terminates": [
                "Action_ZoneBlock",
                "Action_ReachBlock",
                "Action_DownBlock",
                "Action_PullBlock",
                "Action_PullLeadBlock",
                "Action_LeadBlock",
                "Action_BlockSecondLevel",
                "Action_RunBlock",
                "Action_PassBlock",
                "Action_CrackBlock",
                "Action_ComboBlock",
                "Action_SplitBlock",
                "Action_ScreenBlock"
            ]
        },
        "Action_PlayEnd": {
            "event_type": "PLAY_END"
        }
    },
    "action_priority_rules": [
        {
            "higher": "Action_BallSnap",
            "lower": "Action_ZoneBlock",
            "when": {"actor_position": "C"},
            "resolution": "shift_lower_start_to_higher_end_plus_one"
        }
    ],
    "validation_duration_thresholds": {
        "Action_ZoneBlock": {"warn_over_frames": 90},
        "Action_BlockSecondLevel": {"warn_over_frames": 90},
        "Action_PullBlock": {"warn_over_frames": 90},
        "Action_LeadBlock": {"warn_over_frames": 90},
        "Action_DownBlock": {"warn_over_frames": 90},
        "Action_ReachBlock": {"warn_over_frames": 90}
    },
    "action_end_rules": {
        "Action_PreSnap": {
            "ends_at_global_action": "Action_BallSnap",
            "fallback_end": "snap_frame_minus_one"
        },
        "Action_BallSnap": {
            "ends_when_any_action_starts": ["Action_SnapReceive"]
        },
        "Action_SnapReceive": {
            "ends_when_same_actor_action_starts": True
        },
        "Action_Handoff": {
            "ends_when_any_action_starts": ["Action_TakeHandoff", "Action_BallCarry"]
        },
        "Action_TakeHandoff": {
            "ends_when_same_actor_action_starts": True
        },
        "Action_BallCarry": {
            "ends_at_result_or_play_end": True
        },
        "Action_ZoneBlock": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_ReachBlock": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_DownBlock": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_PullBlock": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_LeadBlock": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_BlockSecondLevel": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_RunBlock": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_FakeHandoff": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_BootAway": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_RunFlatRoute": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_ThrowPass": {
            "ends_when_same_actor_action_starts": True,
            "fallback_end": "play_end_frame"
        },
        "Action_SecureCatch": {
            "ends_at_result_or_play_end": True,
            "fallback_end": "play_end_frame"
        },
        "Action_PlayEnd": {
            "ends_at_final_frame": True
        }
    }
}

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration from a YAML file, merging it with defaults."""
    config = merge_dicts(DEFAULT_CONFIG, {})

    # Load timing rules YAML if present beside default_config or in configs/
    for timing_candidate in ["configs/action_timing_rules.yaml", "action_timing_rules.yaml"]:
        if os.path.exists(timing_candidate):
            with open(timing_candidate, "r") as tf:
                timing_cfg = yaml.safe_load(tf)
                if timing_cfg:
                    config = merge_dicts(config, timing_cfg)
            break

    if config_path and os.path.exists(config_path):
        with open(config_path, "r") as f:
            user_config = yaml.safe_load(f)
            if user_config:
                config = merge_dicts(config, user_config)
    return config

def merge_dicts(d1: Dict[str, Any], d2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries."""
    result = d1.copy()
    for k, v in d2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = merge_dicts(result[k], v)
        else:
            result[k] = v
    return result
