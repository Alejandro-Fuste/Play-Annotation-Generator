# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PinAndPull_8`
- **Input XML**: `outputs/batch/PinAndPull/PinAndPull/PinAndPull_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 18: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 93 frames exceeds threshold 90 frames [start=67, end=159].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [65–80], lower_priority='Action_DownBlock' annotated_start=67, effective_Action_DownBlock_start=81.
> - Validation warning: Action 'Action_PullBlock' for track '17' (LG) duration 93 frames exceeds threshold 90 frames [start=67, end=159].
> - Action 'Action_None' range [65-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-102] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-179] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-126] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-175] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [91-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [67-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [131-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [67-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [120-159] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-172] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-163] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-139] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-180] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-169] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-175] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-180] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '27' has 1 frames without a visible bounding box.
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