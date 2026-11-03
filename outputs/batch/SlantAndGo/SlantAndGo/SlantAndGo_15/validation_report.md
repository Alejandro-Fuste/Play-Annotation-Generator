# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_15`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 28: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [1–17], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=18.
> - Action 'Action_None' range [1-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-50] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-61] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-127] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-25] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '15' starts at frame 18, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [18-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-57] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [128-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-79] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-144] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-33] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-17] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '26' has 2 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.