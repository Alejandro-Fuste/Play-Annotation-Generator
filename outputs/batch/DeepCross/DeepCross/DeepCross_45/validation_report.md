# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_45`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_ThrowPass' for track '16' has invalid range: start=111, end=99. Clamping end to start.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [14–29], lower_priority='Action_PassBlock' annotated_start=17, effective_Action_PassBlock_start=30.
> - Action 'Action_None' range [14-329] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-192] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-164] for track '4' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [14-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-200] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [113-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-134] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-262] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-128] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-324] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-37] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-80] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-99] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-68] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-155] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-23] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-42] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-95] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [134-144] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-151] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-132] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '28' has 1 frames without a visible bounding box.
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