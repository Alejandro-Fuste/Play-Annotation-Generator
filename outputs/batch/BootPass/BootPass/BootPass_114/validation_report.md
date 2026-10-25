# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_114`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_114/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 95, Column 'Run Flat Route': Could not parse frame number from 'Drag' in entry 'Drag,21'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 208: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_RunBlock' for track '4' has invalid range: start=63, end=36. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '4' has invalid range: start=145, end=114. Clamping end to start.
> - Segment 'Action_RunBlock' for track '12' has invalid range: start=63, end=62. Clamping end to start.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [37–68], lower_priority='Action_RunBlock' annotated_start=63, effective_Action_RunBlock_start=69.
> - Segment 'Action_SecureCatch' for track '25' has invalid range: start=194, end=112. Clamping end to start.
> - Action 'Action_None' range [37-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-149] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-125] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-152] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-284] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [287-290] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [97-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-249] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-250] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-278] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [37-105] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-299] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [63-97] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [114-201] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [203-299] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [63-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [72-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [78-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [69-88] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [37-138] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-153] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [156-166] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-103] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-235] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-279] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-225] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-290] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-294] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-285] for track '33' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.