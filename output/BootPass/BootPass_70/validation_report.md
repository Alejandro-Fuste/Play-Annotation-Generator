# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_70`
- **Input XML**: `output/BootPass/BootPass_70/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 68 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_BootAway' for track '8' has invalid range: start=98, end=91. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '8' has invalid range: start=156, end=91. Clamping end to start.
> - Action 'Action_PreSnap' range [0-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-172] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [82-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-154] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-198] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-4] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-11] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-172] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-86] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-225] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-239] for track '20' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.