# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_16`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 34: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 34: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 34: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 34: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [2-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-59] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-120] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-11] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-36] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-40] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-10] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-21] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-10] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-17] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-13] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-27] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-9] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-34] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-71] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-63] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-120] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-82] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '27' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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