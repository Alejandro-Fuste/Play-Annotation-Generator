# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_18`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_18/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [39–57], lower_priority='Action_DownBlock' annotated_start=46, effective_Action_DownBlock_start=58.
> - Action 'Action_None' range [39-73] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [80-131] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [134-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [46-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [46-56] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [59-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-91] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [46-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [58-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [46-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-164] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-178] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '21' has 1 frames without a visible bounding box.
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