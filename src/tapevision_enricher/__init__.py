"""
Backward compatibility shim for tapevision_enricher.
This project has been renamed to play_annotation_generator.
"""
import sys
import warnings
import importlib.util
import play_annotation_generator
from play_annotation_generator import (
    run_enrichment_pipeline,
    parse_cvat_xml,
    parse_wide_action_csv,
    parse_cell_entries,
    normalize_and_match_events,
    infer_action_segments,
    run_validation_checks,
)

class _CompatibilityFinder:
    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        if fullname.startswith("tapevision_enricher."):
            target_name = "play_annotation_generator." + fullname[len("tapevision_enricher."):]
            return importlib.util.find_spec(target_name)
        return None

sys.meta_path.insert(0, _CompatibilityFinder)

__all__ = [
    "run_enrichment_pipeline",
    "parse_cvat_xml",
    "parse_wide_action_csv",
    "parse_cell_entries",
    "normalize_and_match_events",
    "infer_action_segments",
    "run_validation_checks",
]
