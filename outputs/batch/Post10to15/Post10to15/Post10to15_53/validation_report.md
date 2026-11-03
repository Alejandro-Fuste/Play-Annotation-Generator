# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_53`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [21–41], lower_priority='Action_PassBlock' annotated_start=24, effective_Action_PassBlock_start=42.
> - Action 'Action_None' range [21-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [41-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [177-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-68] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-110] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-162] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-180] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [21-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-96] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-177] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [42-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [21-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-46] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [107-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-111] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-110] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-166] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-172] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.