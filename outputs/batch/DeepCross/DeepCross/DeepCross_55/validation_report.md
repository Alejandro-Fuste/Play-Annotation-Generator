# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_55`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 58: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 58: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [4–9], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=10.
> - Action 'Action_None' range [4-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-276] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-191] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-213] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-263] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-281] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [283-288] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-260] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [18-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [165-258] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-232] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-128] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-197] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-51] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-216] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-44] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-28] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-200] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-39] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-167] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-92] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-212] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-118] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-214] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-149] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-181] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-163] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-197] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '33' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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