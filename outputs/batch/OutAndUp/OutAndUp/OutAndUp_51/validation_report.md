# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_51`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [24–38], lower_priority='Action_PassBlock' annotated_start=27, effective_Action_PassBlock_start=39.
> - Action 'Action_None' range [24-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-220] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-60] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-142] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [193-240] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-226] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-234] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [24-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-241] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-143] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-186] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-266] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-242] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [24-252] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SellOut' range [74-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [98-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-154] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [157-160] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [168-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [171-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [185-189] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [196-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-152] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [156-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-79] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-130] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-241] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-227] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-198] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-222] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-269] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.