# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_63`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [1–20], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=21.
> - Action 'Action_RunPostRoute' range [20-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-64] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-94] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-67] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-14] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-130] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-158] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '28' has 1 frames without a visible bounding box.
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