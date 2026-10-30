# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_31`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 64: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 64: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 64: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Row 64: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 64: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [15-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-37] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-53] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-33] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-90] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-78] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [15-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-55] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-56] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-31] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-53] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-90] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [31-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-90] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-90] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-90] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '27' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.