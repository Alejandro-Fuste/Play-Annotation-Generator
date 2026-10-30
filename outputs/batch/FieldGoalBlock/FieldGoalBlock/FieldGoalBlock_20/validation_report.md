# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_20`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 42: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 42: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 42: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [2-261] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-219] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-274] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-45] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-49] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-44] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-185] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-62] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-18] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-28] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-40] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-94] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-21] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-79] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-24] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [2-16] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-58] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-18] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-30] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-38] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-131] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-52] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [58-64] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-294] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-48] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-62] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-18] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-207] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-43] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-52] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-90] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-140] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-105] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-261] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-195] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-123] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-255] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-118] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-146] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-203] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '34' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.