import os
import tempfile
import unittest
from play_annotation_generator.cvat_xml_parser import parse_cvat_xml

MOCK_XML = """<?xml version="1.0" encoding="utf-8"?>
<annotations>
  <version>1.1</version>
  <meta>
    <job>
      <id>12345</id>
      <size>100</size>
      <mode>interpolation</mode>
      <start_frame>0</start_frame>
      <stop_frame>99</stop_frame>
    </job>
    <original_size>
      <width>1920</width>
      <height>1080</height>
    </original_size>
  </meta>
  <track id="0" label="player" source="manual">
    <box frame="0" keyframe="1" outside="0" occluded="0" xtl="10.0" ytl="20.0" xbr="30.0" ybr="40.0">
      <attribute name="position">QB</attribute>
      <attribute name="team_side">offense</attribute>
      <attribute name="track_id">12</attribute>
    </box>
    <box frame="1" keyframe="1" outside="0" occluded="0" xtl="11.0" ytl="21.0" xbr="31.0" ybr="41.0">
      <attribute name="position">QB</attribute>
      <attribute name="team_side">offense</attribute>
      <attribute name="track_id">12</attribute>
    </box>
  </track>
  <track id="1" label="ball" source="file">
    <box frame="0" keyframe="1" outside="0" occluded="0" xtl="5.0" ytl="5.0" xbr="8.0" ybr="8.0">
      <attribute name="ball_status">pre_snap</attribute>
    </box>
  </track>
</annotations>
"""

class TestCVATXMLParser(unittest.TestCase):
    def setUp(self):
        self.temp_xml = tempfile.NamedTemporaryFile(suffix=".xml", delete=False)
        self.temp_xml.write(MOCK_XML.encode("utf-8"))
        self.temp_xml.close()

    def tearDown(self):
        os.unlink(self.temp_xml.name)

    def test_parse_metadata(self):
        _, metadata = parse_cvat_xml(self.temp_xml.name)
        self.assertEqual(metadata["width"], 1920)
        self.assertEqual(metadata["height"], 1080)
        self.assertEqual(metadata["total_frames"], 100)
        self.assertEqual(metadata["start_frame"], 0)
        self.assertEqual(metadata["stop_frame"], 99)

    def test_parse_tracks(self):
        tracks, _ = parse_cvat_xml(self.temp_xml.name)
        self.assertIn("0", tracks)
        self.assertIn("1", tracks)
        
        player_track = tracks["0"]
        self.assertEqual(player_track.label, "player")
        self.assertEqual(player_track.position, "QB")
        self.assertEqual(player_track.team_side, "offense")
        self.assertEqual(player_track.custom_track_id, "12")
        
        box0 = player_track.boxes_by_frame[0]
        self.assertEqual(box0.xtl, 10.0)
        self.assertEqual(box0.ytl, 20.0)
        self.assertFalse(box0.outside)
        self.assertEqual(box0.attributes.get("position"), "QB")
        
        ball_track = tracks["1"]
        self.assertEqual(ball_track.label, "ball")
        self.assertIsNone(ball_track.position)

if __name__ == "__main__":
    unittest.main()
