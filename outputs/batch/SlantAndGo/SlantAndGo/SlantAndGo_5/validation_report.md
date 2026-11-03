# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_5`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [10–25], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=26.
> - Action 'Action_PassBlock' range [18-35] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-45] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-49] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [65-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-146] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-32] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-144] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-87] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-94] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [83-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [121-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-26] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-149] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-150] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.