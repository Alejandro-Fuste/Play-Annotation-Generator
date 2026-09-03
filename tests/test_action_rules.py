import unittest
from tapevision_enricher.models import ActionEvent, Track, TrackBox
from tapevision_enricher.action_rules import infer_action_segments
from tapevision_enricher.config import DEFAULT_CONFIG

class TestActionRules(unittest.TestCase):
    def setUp(self):
        self.config = DEFAULT_CONFIG.copy()
        self.metadata = {
            "start_frame": 0,
            "stop_frame": 239,
            "total_frames": 240
        }

    def _create_mock_track(self, xml_id="0", custom_id="13", position="RT", team_side="offense", num_frames=240):
        track = Track(xml_track_id=xml_id, label="player", source="manual", custom_track_id=custom_id, position=position, team_side=team_side)
        for f in range(num_frames):
            track.boxes_by_frame[f] = TrackBox(frame=f, xtl=10, ytl=10, xbr=50, ybr=50, outside=False, occluded=False, keyframe=False)
        return track

    def test_jetsweep_rt_sequential_actions(self):
        # JetSweep RT: PreSnap 0-132, ZoneBlock 133-164, BlockSecondLevel 165-192 (inclusive boundary), Action_None 193-239
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=132, start_frame=132, actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_ZoneBlock", annotated_frame=133, start_frame=133, actor_track_id="13", resolved_xml_track_id="13_xml", target_kind="track_id"),
            ActionEvent(action="Action_BlockSecondLevel", annotated_frame=165, start_frame=165, actor_track_id="13", resolved_xml_track_id="13_xml", target_kind="track_id"),
            ActionEvent(action="Action_None", annotated_frame=192, start_frame=192, actor_track_id="13", resolved_xml_track_id="13_xml", target_kind="track_id", event_type="BOUNDARY", annotated_frame_role="BOUNDARY")
        ]
        track_rt = self._create_mock_track(xml_id="13_xml", custom_id="13", position="RT")
        track_c = self._create_mock_track(xml_id="7_xml", custom_id="7", position="C")
        tracks = {"13_xml": track_rt, "7_xml": track_c}

        segments, warnings = infer_action_segments(events, tracks, self.metadata, self.config)
        rt_segs = sorted([s for s in segments if s.xml_track_id == "13_xml"], key=lambda x: x.start_frame)

        self.assertEqual(len(rt_segs), 4)
        self.assertEqual((rt_segs[0].action, rt_segs[0].start_frame, rt_segs[0].end_frame), ("Action_PreSnap", 0, 132))
        self.assertEqual((rt_segs[1].action, rt_segs[1].start_frame, rt_segs[1].end_frame), ("Action_ZoneBlock", 133, 164))
        self.assertEqual((rt_segs[2].action, rt_segs[2].start_frame, rt_segs[2].end_frame), ("Action_BlockSecondLevel", 165, 192))
        self.assertEqual((rt_segs[3].action, rt_segs[3].start_frame, rt_segs[3].end_frame), ("Action_None", 193, 239))

    def test_rg_sequential_actions(self):
        # RG: PreSnap -> ZoneBlock -> BlockSecondLevel -> Action_None
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=132, start_frame=132, actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_ZoneBlock", annotated_frame=133, start_frame=133, actor_track_id="10", resolved_xml_track_id="10_xml", target_kind="track_id"),
            ActionEvent(action="Action_BlockSecondLevel", annotated_frame=165, start_frame=165, actor_track_id="10", resolved_xml_track_id="10_xml", target_kind="track_id"),
            ActionEvent(action="Action_None", annotated_frame=192, start_frame=192, actor_track_id="10", resolved_xml_track_id="10_xml", target_kind="track_id", event_type="BOUNDARY", annotated_frame_role="BOUNDARY")
        ]
        track_rg = self._create_mock_track(xml_id="10_xml", custom_id="10", position="RG")
        track_c = self._create_mock_track(xml_id="7_xml", custom_id="7", position="C")
        tracks = {"10_xml": track_rg, "7_xml": track_c}

        segments, _ = infer_action_segments(events, tracks, self.metadata, self.config)
        rg_segs = sorted([s for s in segments if s.xml_track_id == "10_xml"], key=lambda x: x.start_frame)

        self.assertEqual(len(rg_segs), 4)
        self.assertEqual((rg_segs[0].action, rg_segs[0].start_frame, rg_segs[0].end_frame), ("Action_PreSnap", 0, 132))
        self.assertEqual((rg_segs[1].action, rg_segs[1].start_frame, rg_segs[1].end_frame), ("Action_ZoneBlock", 133, 164))
        self.assertEqual((rg_segs[2].action, rg_segs[2].start_frame, rg_segs[2].end_frame), ("Action_BlockSecondLevel", 165, 192))
        self.assertEqual((rg_segs[3].action, rg_segs[3].start_frame, rg_segs[3].end_frame), ("Action_None", 193, 239))

    def test_toss_cross_actor_ending(self):
        # Action_Toss (145, QB/17) ends at frame 159 before Action_BallCarry (160, WR/19)
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=132, start_frame=132, annotated_frame_role="START", actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_SnapReceive", annotated_frame=144, start_frame=144, annotated_frame_role="END", actor_track_id="17", resolved_xml_track_id="17_xml", target_kind="track_id"),
            ActionEvent(action="Action_Toss", annotated_frame=145, start_frame=145, annotated_frame_role="START", actor_track_id="17", resolved_xml_track_id="17_xml", target_kind="track_id"),
            ActionEvent(action="Action_BallCarry", annotated_frame=160, start_frame=160, annotated_frame_role="START", actor_track_id="19", resolved_xml_track_id="19_xml", target_kind="track_id")
        ]
        track_qb = self._create_mock_track(xml_id="17_xml", custom_id="17", position="QB")
        track_wr = self._create_mock_track(xml_id="19_xml", custom_id="19", position="WR")
        tracks = {"17_xml": track_qb, "19_xml": track_wr}

        segments, _ = infer_action_segments(events, tracks, self.metadata, self.config)
        qb_toss = [s for s in segments if s.xml_track_id == "17_xml" and s.action == "Action_Toss"][0]
        self.assertEqual((qb_toss.start_frame, qb_toss.end_frame), (145, 159))

    def test_ball_carry_final_clip_fallback(self):
        # Action_BallCarry continues to stop_clip (239) with NO trailing Action_None
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=132, start_frame=132, actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_BallCarry", annotated_frame=160, start_frame=160, actor_track_id="19", resolved_xml_track_id="19_xml", target_kind="track_id")
        ]
        track_wr = self._create_mock_track(xml_id="19_xml", custom_id="19", position="WR")
        tracks = {"19_xml": track_wr}

        segments, _ = infer_action_segments(events, tracks, self.metadata, self.config)
        wr_segs = sorted([s for s in segments if s.xml_track_id == "19_xml"], key=lambda x: x.start_frame)
        self.assertEqual(len(wr_segs), 2)
        self.assertEqual((wr_segs[0].action, wr_segs[0].start_frame, wr_segs[0].end_frame), ("Action_PreSnap", 0, 159))
        self.assertEqual((wr_segs[1].action, wr_segs[1].start_frame, wr_segs[1].end_frame), ("Action_BallCarry", 160, 239))

    def test_lead_block_inclusive_ol_boundary(self):
        # Action_LeadBlock 133-192, Action_None 193-239
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=132, start_frame=132, actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_LeadBlock", annotated_frame=133, start_frame=133, actor_track_id="12", resolved_xml_track_id="12_xml", target_kind="track_id"),
            ActionEvent(action="Action_None", annotated_frame=192, start_frame=192, actor_track_id="12", resolved_xml_track_id="12_xml", target_kind="track_id", event_type="BOUNDARY", annotated_frame_role="BOUNDARY")
        ]
        track_te = self._create_mock_track(xml_id="12_xml", custom_id="12", position="TE")
        tracks = {"12_xml": track_te}

        segments, _ = infer_action_segments(events, tracks, self.metadata, self.config)
        te_segs = sorted([s for s in segments if s.xml_track_id == "12_xml"], key=lambda x: x.start_frame)
        self.assertEqual(len(te_segs), 3)
        self.assertEqual((te_segs[0].action, te_segs[0].start_frame, te_segs[0].end_frame), ("Action_PreSnap", 0, 132))
        self.assertEqual((te_segs[1].action, te_segs[1].start_frame, te_segs[1].end_frame), ("Action_LeadBlock", 133, 192))
        self.assertEqual((te_segs[2].action, te_segs[2].start_frame, te_segs[2].end_frame), ("Action_None", 193, 239))

    def test_center_priority_resolution(self):
        # Center: BallSnap 132-144, ZoneBlock shifts start to 145, ends at 192
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=132, start_frame=132, annotated_frame_role="START", actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_SnapReceive", annotated_frame=144, start_frame=144, annotated_frame_role="END", actor_track_id="17", resolved_xml_track_id="17_xml", target_kind="track_id"),
            ActionEvent(action="Action_ZoneBlock", annotated_frame=133, start_frame=133, actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_None", annotated_frame=192, start_frame=192, actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id", event_type="BOUNDARY", annotated_frame_role="BOUNDARY")
        ]
        track_c = self._create_mock_track(xml_id="7_xml", custom_id="7", position="C")
        tracks = {"7_xml": track_c}

        segments, warnings = infer_action_segments(events, tracks, self.metadata, self.config)
        c_segs = sorted([s for s in segments if s.xml_track_id == "7_xml"], key=lambda x: x.start_frame)
        self.assertEqual(len(c_segs), 4)
        self.assertEqual((c_segs[0].action, c_segs[0].start_frame, c_segs[0].end_frame), ("Action_PreSnap", 0, 131))
        self.assertEqual((c_segs[1].action, c_segs[1].start_frame, c_segs[1].end_frame), ("Action_BallSnap", 132, 144))
        self.assertEqual((c_segs[2].action, c_segs[2].start_frame, c_segs[2].end_frame), ("Action_ZoneBlock", 145, 192))
        self.assertEqual((c_segs[3].action, c_segs[3].start_frame, c_segs[3].end_frame), ("Action_None", 193, 239))
        self.assertTrue(any("Resolved action overlap" in w for w in warnings))

    def test_ball_snap_snap_receive_paired_interval(self):
        # Ball Snap = 132,7 (C), Snap Receive = 144,17 (QB)
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=132, start_frame=132, annotated_frame_role="START", actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_SnapReceive", annotated_frame=144, start_frame=144, annotated_frame_role="END", actor_track_id="17", resolved_xml_track_id="17_xml", target_kind="track_id")
        ]
        track_c = self._create_mock_track(xml_id="7_xml", custom_id="7", position="C")
        track_qb = self._create_mock_track(xml_id="17_xml", custom_id="17", position="QB")
        tracks = {"7_xml": track_c, "17_xml": track_qb}

        segments, _ = infer_action_segments(events, tracks, self.metadata, self.config)

        c_snap = [s for s in segments if s.xml_track_id == "7_xml" and s.action == "Action_BallSnap"][0]
        qb_snap = [s for s in segments if s.xml_track_id == "17_xml" and s.action == "Action_SnapReceive"][0]

        self.assertEqual((c_snap.start_frame, c_snap.end_frame), (132, 144))
        self.assertEqual((qb_snap.start_frame, qb_snap.end_frame), (132, 144))

    def test_qb_next_action_after_snap_receive(self):
        # QB: PreSnap 0-131, SnapReceive 132-144, Toss 145-239
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=132, start_frame=132, annotated_frame_role="START", actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_SnapReceive", annotated_frame=144, start_frame=144, annotated_frame_role="END", actor_track_id="17", resolved_xml_track_id="17_xml", target_kind="track_id"),
            ActionEvent(action="Action_Toss", annotated_frame=145, start_frame=145, annotated_frame_role="START", actor_track_id="17", resolved_xml_track_id="17_xml", target_kind="track_id")
        ]
        track_c = self._create_mock_track(xml_id="7_xml", custom_id="7", position="C")
        track_qb = self._create_mock_track(xml_id="17_xml", custom_id="17", position="QB")
        tracks = {"7_xml": track_c, "17_xml": track_qb}

        segments, _ = infer_action_segments(events, tracks, self.metadata, self.config)
        qb_segs = sorted([s for s in segments if s.xml_track_id == "17_xml"], key=lambda x: x.start_frame)

        self.assertEqual(len(qb_segs), 3)
        self.assertEqual((qb_segs[0].action, qb_segs[0].start_frame, qb_segs[0].end_frame), ("Action_PreSnap", 0, 131))
        self.assertEqual((qb_segs[1].action, qb_segs[1].start_frame, qb_segs[1].end_frame), ("Action_SnapReceive", 132, 144))
        self.assertEqual((qb_segs[2].action, qb_segs[2].start_frame, qb_segs[2].end_frame), ("Action_Toss", 145, 239))

    def test_uninvolved_wr_and_defense(self):
        # Uninvolved WR and Defender get PreSnap then Action_None
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=132, start_frame=132, actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id")
        ]
        track_wr = self._create_mock_track(xml_id="wr_xml", custom_id="1", position="WR-X", team_side="offense")
        track_cb = self._create_mock_track(xml_id="cb_xml", custom_id="21", position="CB", team_side="defense")
        track_c = self._create_mock_track(xml_id="7_xml", custom_id="7", position="C", team_side="offense")
        tracks = {"wr_xml": track_wr, "cb_xml": track_cb, "7_xml": track_c}

        segments, _ = infer_action_segments(events, tracks, self.metadata, self.config)
        wr_segs = sorted([s for s in segments if s.xml_track_id == "wr_xml"], key=lambda x: x.start_frame)
        cb_segs = sorted([s for s in segments if s.xml_track_id == "cb_xml"], key=lambda x: x.start_frame)

        self.assertEqual(len(wr_segs), 2)
        self.assertEqual((wr_segs[0].action, wr_segs[0].start_frame, wr_segs[0].end_frame), ("Action_PreSnap", 0, 131))
        self.assertEqual((wr_segs[1].action, wr_segs[1].start_frame, wr_segs[1].end_frame), ("Action_None", 132, 239))

        self.assertEqual(len(cb_segs), 2)
        self.assertEqual((cb_segs[0].action, cb_segs[0].start_frame, cb_segs[0].end_frame), ("Action_PreSnap", 0, 131))
        self.assertEqual((cb_segs[1].action, cb_segs[1].start_frame, cb_segs[1].end_frame), ("Action_None", 132, 239))

    def test_complete_frame_coverage(self):
        # Every visible mapped player frame has count(primary_action_labels) == 1
        events = [
            ActionEvent(action="Action_BallSnap", annotated_frame=100, start_frame=100, actor_track_id="7", resolved_xml_track_id="7_xml", target_kind="track_id"),
            ActionEvent(action="Action_ZoneBlock", annotated_frame=105, start_frame=105, actor_track_id="13", resolved_xml_track_id="13_xml", target_kind="track_id")
        ]
        track1 = self._create_mock_track(xml_id="13_xml", custom_id="13", position="RT", num_frames=200)
        track2 = self._create_mock_track(xml_id="7_xml", custom_id="7", position="C", num_frames=200)
        tracks = {"13_xml": track1, "7_xml": track2}

        segments, _ = infer_action_segments(events, tracks, self.metadata, self.config)

        for xml_id in ["13_xml", "7_xml"]:
            track_segs = [s for s in segments if s.xml_track_id == xml_id]
            frame_coverage = {}
            for s in track_segs:
                for f in range(s.start_frame, s.end_frame + 1):
                    frame_coverage[f] = frame_coverage.get(f, 0) + 1

            for f in range(200):
                self.assertEqual(frame_coverage.get(f, 0), 1, f"Frame {f} for track {xml_id} does not have exactly 1 primary action")

if __name__ == "__main__":
    unittest.main()
