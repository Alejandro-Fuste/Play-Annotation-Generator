# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_17`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 19: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [10–14], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=15.
> - Action 'Action_None' range [10-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-206] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-35] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [168-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-196] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-144] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [149-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [161-204] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [206-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-51] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-152] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-187] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [10-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-77] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-123] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [105-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [112-159] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [174-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [112-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-80] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [88-93] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-152] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '27' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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