# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_15`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [25–37], lower_priority='Action_PassBlock' annotated_start=31, effective_Action_PassBlock_start=38.
> - Action 'Action_RunPostRoute' range [50-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-62] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-176] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [25-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-130] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [25-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-180] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [25-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-99] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-154] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-75] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-180] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-76] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-88] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-152] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-162] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-97] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-180] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-171] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
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