# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_72`
- **Input XML**: `output/BootPass/BootPass_72/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 41 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_ThrowPass' for track '0' has invalid range: start=126, end=121. Clamping end to start.
> - Action 'Action_PreSnap' range [0-121] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-169] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-9] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-91] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-66] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-80] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-126] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-197] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-97] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-130] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-85] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-197] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-209] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-156] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.