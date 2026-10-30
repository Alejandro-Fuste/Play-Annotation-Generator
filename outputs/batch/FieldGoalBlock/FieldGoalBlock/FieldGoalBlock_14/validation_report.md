# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_14`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_14/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 30: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [6-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-85] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-24] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-70] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-34] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-111] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-64] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-23] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-78] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-26] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-31] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-58] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-4] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-23] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-24] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-57] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-87] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-144] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-53] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-92] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-143] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-115] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-150] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-127] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-131] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-135] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-135] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-150] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.