import unittest
from play_annotation_generator.models import ActionEvent, ActionSegment, Track, TrackBox
from play_annotation_generator.validators import run_validation_checks
from play_annotation_generator.config import DEFAULT_CONFIG

class TestValidators(unittest.TestCase):
    def setUp(self):
        self.config = DEFAULT_CONFIG
        self.metadata = {
            "start_frame": 0,
            "stop_frame": 100,
            "total_frames": 101
        }

    def test_invalid_box_coordinates(self):
        # Create a track with one invalid box (xbr <= xtl)
        track = Track(xml_track_id="0", label="player", source="manual", custom_track_id="2")
        track.boxes_by_frame[0] = TrackBox(frame=0, xtl=50.0, ytl=50.0, xbr=40.0, ybr=60.0, outside=False, occluded=False, keyframe=False)
        tracks = {"0": track}
        
        metrics, warnings, errors = run_validation_checks(tracks, [], [], self.metadata, self.config)
        
        self.assertEqual(metrics["num_invalid_boxes"], 1)
        self.assertTrue(any("invalid bounding box" in w for w in warnings))

    def test_overlapping_segments_validation(self):
        # Create overlapping segments for the same track ID
        segments = [
            ActionSegment(actor_track_id="2", xml_track_id="0", position="QB", team_side="offense", action="Action_ZoneBlock", start_frame=10, end_frame=20, source="test"),
            ActionSegment(actor_track_id="2", xml_track_id="0", position="QB", team_side="offense", action="Action_LeadBlock", start_frame=15, end_frame=25, source="test")
        ]
        
        track = Track(xml_track_id="0", label="player", source="manual", custom_track_id="2")
        tracks = {"0": track}
        
        _, _, errors = run_validation_checks(tracks, [], segments, self.metadata, self.config)
        
        self.assertTrue(any("Overlapping action segments" in e for e in errors))

    def test_undefined_track_attributes(self):
        # Create a player track with 'undefined' position and team_side
        track = Track(xml_track_id="0", label="player", source="manual", position="undefined", team_side="undefined")
        tracks = {"0": track}
        
        _, warnings, _ = run_validation_checks(tracks, [], [], self.metadata, self.config)
        
        self.assertTrue(any("undefined position" in w for w in warnings))
        self.assertTrue(any("undefined team_side" in w for w in warnings))

if __name__ == "__main__":
    unittest.main()
