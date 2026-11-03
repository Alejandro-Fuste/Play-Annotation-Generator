# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_17`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 29: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - Row 30: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 30: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [13–26], lower_priority='Action_PassBlock' annotated_start=17, effective_Action_PassBlock_start=27.
> - Segment 'Action_PassBlock' for track '16' has invalid range: start=17, end=12. Clamping end to start.
> - Action 'Action_None' range [13-109] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-170] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [88-173] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [175-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [179-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-73] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-83] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-193] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-67] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-170] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-50] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [13-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [85-149] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-174] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-178] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-135] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-106] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-83] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [121-135] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-122] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [101-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-109] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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