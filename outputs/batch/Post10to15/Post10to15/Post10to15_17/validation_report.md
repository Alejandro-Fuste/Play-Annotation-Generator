# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_17`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
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
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [18–33], lower_priority='Action_PassBlock' annotated_start=21, effective_Action_PassBlock_start=34.
> - Action 'Action_RunPostRoute' range [33-49] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [51-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-67] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-100] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-117] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-140] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-138] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-91] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [130-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-201] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-237] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-115] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [120-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [90-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-140] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-116] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-150] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.