# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_62`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [49–65], lower_priority='Action_PassBlock' annotated_start=52, effective_Action_PassBlock_start=66.
> - Action 'Action_PassBlock' range [52-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-77] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-96] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-186] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [192-234] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-52] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-99] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-182] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-167] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-156] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-232] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '28' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.