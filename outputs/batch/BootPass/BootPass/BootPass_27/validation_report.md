# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_27`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [23–34], lower_priority='Action_RunBlock' annotated_start=29, effective_Action_RunBlock_start=35.
> - Action 'Action_None' range [23-89] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [108-237] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-90] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [29-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [46-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [29-75] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [84-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [100-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [106-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [134-166] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [169-170] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-184] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [29-37] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-176] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-204] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-231] for track '28' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.