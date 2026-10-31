# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_62`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 72: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [15–30], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=31.
> - Action 'Action_RunHitchRoute' range [30-107] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [134-142] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-56] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-73] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-72] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-50] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-65] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-50] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-50] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [15-27] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-110] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-50] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-59] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-209] for track '21' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-174] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-209] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-209] for track '32' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.