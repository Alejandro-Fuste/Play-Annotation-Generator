# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_5`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [21–35], lower_priority='Action_PassBlock' annotated_start=24, effective_Action_PassBlock_start=36.
> - Action 'Action_None' range [21-237] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-58] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-67] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-231] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-239] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [21-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-82] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-87] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-231] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-233] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-226] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [230-236] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [229-230] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [235-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-80] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-73] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-231] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-226] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-141] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-221] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-223] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-237] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [227-232] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-235] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [227-234] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.