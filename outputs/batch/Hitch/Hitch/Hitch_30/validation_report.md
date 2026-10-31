# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_30`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [1–14], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=15.
> - Action 'Action_BallCarry' range [130-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [184-223] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [225-230] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-217] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-214] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-215] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-173] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-182] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-184] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-74] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-185] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-188] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-100] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-103] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-239] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-63] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-74] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-90] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-113] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-198] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-206] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-174] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-164] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-173] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.