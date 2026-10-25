# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_76`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 23 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [29–45], lower_priority='Action_RunBlock' annotated_start=35, effective_Action_RunBlock_start=46.
> - Action 'Action_None' range [161-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-73] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [46-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-47] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [50-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-54] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [67-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-158] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [101-149] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [152-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [158-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-43] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-51] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-103] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '29' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.