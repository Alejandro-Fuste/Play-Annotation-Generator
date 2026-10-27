# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_22`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Overlapping action conflict at frame 42 for track '2': 'Action_PlaySideFakeStep' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
> - Validation warning: Action 'Action_DownBlock' for track '11' (TE) duration 113 frames exceeds threshold 90 frames [start=42, end=154].
> - Validation warning: Action 'Action_PullBlock' for track '13' (LG) duration 110 frames exceeds threshold 90 frames [start=42, end=151].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [39–55], lower_priority='Action_DownBlock' annotated_start=42, effective_Action_DownBlock_start=56.
> - Action 'Action_None' range [39-188] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [91-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-82] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-206] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [42-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [42-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [62-63] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [65-73] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [75-147] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [149-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [39-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-86] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-103] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '27' has 1 frames without a visible bounding box.
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