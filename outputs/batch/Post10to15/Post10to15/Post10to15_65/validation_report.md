# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_65`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
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
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [8–21], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=22.
> - Action 'Action_None' range [8-52] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-126] for track '0' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-62] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-154] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [21-180] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-156] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-81] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-131] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-28] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-34] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-55] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-99] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [115-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-36] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [131-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-18] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-74] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-124] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [149-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-43] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-141] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [67-80] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-141] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-119] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-157] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.