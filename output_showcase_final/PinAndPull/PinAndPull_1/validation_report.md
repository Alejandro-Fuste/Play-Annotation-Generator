# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PinAndPull_1`
- **Input XML**: `output_showcase_final/PinAndPull/PinAndPull_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 4: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '4' has invalid range: start=41, end=28. Clamping end to start.
> - Validation warning: Action 'Action_DownBlock' for track '11' (RT) duration 97 frames exceeds threshold 90 frames [start=13, end=109].
> - Validation warning: Action 'Action_PullBlock' for track '21' (C) duration 97 frames exceeds threshold 90 frames [start=13, end=109].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [10–23], lower_priority='Action_PullBlock' annotated_start=13, effective_Action_PullBlock_start=24.
> - Action 'Action_None' range [41-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-120] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-43] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-120] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-22] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-120] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-100] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-120] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-21] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-26] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-79] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [13-45] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [48-109] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [13-90] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-107] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-80] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-30] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-77] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [79-118] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-93] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-120] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-78] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-24] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [24-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [105-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-41] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-109] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-56] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-120] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '29' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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