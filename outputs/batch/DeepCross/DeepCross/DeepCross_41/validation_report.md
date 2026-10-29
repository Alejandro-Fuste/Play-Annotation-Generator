# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_41`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 44: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [17–30], lower_priority='Action_PassBlock' annotated_start=20, effective_Action_PassBlock_start=31.
> - Action 'Action_RunDeepCrossRoute' range [30-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-246] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-262] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-43] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-55] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-245] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-246] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-269] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-241] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-64] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-205] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-85] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [167-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-240] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-151] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-238] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-261] for track '28' has 3 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.