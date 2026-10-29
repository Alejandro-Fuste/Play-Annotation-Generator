# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_87`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_87/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 90: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 90: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 90: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - Row 90: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [9–15], lower_priority='Action_PassBlock' annotated_start=12, effective_Action_PassBlock_start=16.
> - Action 'Action_None' range [9-96] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-193] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-59] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-155] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-67] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-159] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-96] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-157] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-59] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-109] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-59] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-160] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-105] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-61] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-163] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [119-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '31' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.