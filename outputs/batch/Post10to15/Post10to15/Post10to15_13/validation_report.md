# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_13`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 16: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [1–9], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=10.
> - Action 'Action_None' range [1-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [17-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [116-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-150] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-148] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-131] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-65] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-132] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-150] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-46] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-107] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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