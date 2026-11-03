# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_13`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 96 |
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
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [8–23], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=24.
> - Action 'Action_None' range [8-54] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [102-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-92] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-64] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-33] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [170-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-122] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-34] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [108-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-164] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [8-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-171] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-164] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [167-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-180] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-10] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-27] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-23] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-29] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-37] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-87] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-158] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-162] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-177] for track '28' has 2 frames without a visible bounding box.
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
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.