# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_49`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
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
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [1–14], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=15.
> - Action 'Action_RunPostRoute' range [14-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [126-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-57] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-63] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-81] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-31] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-136] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-156] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-106] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-29] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-73] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-71] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-63] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-70] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-117] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-136] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-180] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-27] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-9] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-41] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-180] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-133] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-162] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-156] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '30' has 1 frames without a visible bounding box.
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