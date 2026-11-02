# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PinAndPull_3`
- **Input XML**: `outputs/batch/PinAndPull/PinAndPull/PinAndPull_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '7' (C) duration 123 frames exceeds threshold 90 frames [start=12, end=134].
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [9–25], lower_priority='Action_PullBlock' annotated_start=12, effective_Action_PullBlock_start=26.
> - Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 123 frames exceeds threshold 90 frames [start=12, end=134].
> - Action 'Action_BallCarry' range [42-180] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-57] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-99] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-157] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-72] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [26-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [12-134] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-147] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-164] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-76] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-180] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-104] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.