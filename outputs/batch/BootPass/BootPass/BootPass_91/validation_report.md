# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_91`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [29–44], lower_priority='Action_RunBlock' annotated_start=36, effective_Action_RunBlock_start=45.
> - Action 'Action_None' range [29-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-57] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [45-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [67-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [36-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [36-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [183-207] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [36-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [36-210] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-89] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-78] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '28' has 1 frames without a visible bounding box.
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