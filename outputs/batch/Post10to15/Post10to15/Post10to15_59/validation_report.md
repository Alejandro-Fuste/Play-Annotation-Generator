# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_59`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 62: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [21–39], lower_priority='Action_PassBlock' annotated_start=24, effective_Action_PassBlock_start=40.
> - Action 'Action_None' range [21-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-134] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-71] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-108] for track '9' has 6 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [125-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [121-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-68] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-123] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-161] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-88] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-170] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [175-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [132-146] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [149-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [39-155] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [157-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-138] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '25' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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