# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_78`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 158: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-58] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-53] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-95] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-38] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-129] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [52-60] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [67-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-77] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-13] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-59] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-28] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-7] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-7] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-5] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-58] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-34] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-180] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [43-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-180] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-141] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-104] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-144] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-163] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-172] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '33' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.