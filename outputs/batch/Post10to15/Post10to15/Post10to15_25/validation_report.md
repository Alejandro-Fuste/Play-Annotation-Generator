# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_25`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [31–46], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=47.
> - Action 'Action_RunPostRoute' range [49-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [122-167] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [170-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-83] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-193] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-67] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-77] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-183] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-139] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [31-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-33] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-17] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-77] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-211] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-116] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-181] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [187-193] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '30' has 1 frames without a visible bounding box.
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