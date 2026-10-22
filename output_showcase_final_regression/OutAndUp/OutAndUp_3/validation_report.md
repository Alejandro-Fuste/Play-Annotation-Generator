# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_3`
- **Input XML**: `output_showcase_final_regression/OutAndUp/OutAndUp_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 6: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [5–21], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=22.
> - Action 'Action_None' range [5-69] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-127] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-202] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-54] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-61] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-188] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [93-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [123-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-181] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' for track '18' starts at frame 103, but the player has no visible bounding box on this frame.
> - Action 'Action_ThrowPass' range [103-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-29] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-114] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-170] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-173] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-184] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-174] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-176] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-191] for track '30' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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