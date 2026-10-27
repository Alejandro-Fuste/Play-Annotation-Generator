# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_290`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_290/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 21 |
| Ball Tracks | 1 |
| CSV events parsed | 18 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Overlapping action conflict at frame 139 for track '4': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [136–151], lower_priority='Action_PullLeadBlock' annotated_start=139, effective_Action_PullLeadBlock_start=152.
> - Action 'Action_None' range [136-283] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [139-181] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-277] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-283] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-251] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [197-246] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [251-255] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [258-276] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [139-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [187-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-222] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [165-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-271] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-283] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-205] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [139-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [163-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-264] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-234] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-250] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-258] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-287] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-164] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-290] for track '16' has 3 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.