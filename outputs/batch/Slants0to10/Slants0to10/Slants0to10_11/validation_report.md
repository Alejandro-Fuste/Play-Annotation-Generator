# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_11`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [15–28], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=29.
> - Action 'Action_None' range [15-58] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-147] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-243] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-88] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-145] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-118] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-59] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-170] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-165] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-155] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-60] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [66-72] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-123] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '28' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.