# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_106`
- **Input XML**: `output/BootPass/BootPass_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 50 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Overlapping action conflict at frame 55 for track '19': 'Action_SnapReceive' vs 'Action_FakeHandoff'. Overriding with 'Action_FakeHandoff'.
> - Segment 'Action_FakeHandoff' for track '19' has invalid range: start=141, end=98. Clamping end to start.
> - Segment 'Action_BootAway' for track '19' has invalid range: start=141, end=128. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '19' has invalid range: start=141, end=139. Clamping end to start.
> - Action 'Action_PreSnap' range [0-70] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-210] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-181] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-156] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [166-189] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-206] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-194] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-197] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-208] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.