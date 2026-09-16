# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_94`
- **Input XML**: `output/BootPass/BootPass_94/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 33 |
| Ball Tracks | 1 |
| CSV events parsed | 7 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 52 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '4' has invalid range: start=180, end=68. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '15' has invalid range: start=62, end=52. Clamping end to start.
> - Action 'Action_PreSnap' range [0-35] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-58] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-105] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-82] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-33] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-60] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-92] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-192] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 63, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [63-67] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-156] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [96-130] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '23' starts at frame 146, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [146-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-189] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-210] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-185] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-210] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.