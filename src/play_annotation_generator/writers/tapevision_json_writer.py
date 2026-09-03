"""
Backward compatibility module for tapevision_json_writer.
"""
from .play_annotation_json_writer import (
    write_play_annotation_json,
    write_tapevision_json,
)

__all__ = ["write_play_annotation_json", "write_tapevision_json"]
