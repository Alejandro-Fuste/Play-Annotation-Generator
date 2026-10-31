# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_18`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_18/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 28: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [20–36], lower_priority='Action_PassBlock' annotated_start=23, effective_Action_PassBlock_start=37.
> - Action 'Action_None' range [20-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [149-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-87] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-57] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-189] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-31] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-40] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-71] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [20-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-63] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-139] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-196] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-48] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-71] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-122] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-187] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '37' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.