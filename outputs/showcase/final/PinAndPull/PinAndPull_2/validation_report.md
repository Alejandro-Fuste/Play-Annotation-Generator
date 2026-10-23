# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PinAndPull_2`
- **Input XML**: `output_showcase_final/PinAndPull/PinAndPull_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 6: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 6: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '3' (DT2) duration 92 frames exceeds threshold 90 frames [start=14, end=105].
> - Validation warning: Action 'Action_PullBlock' for track '9' (RG) duration 92 frames exceeds threshold 90 frames [start=14, end=105].
> - Segment 'Action_BallCarry' for track '10' has invalid range: start=41, end=40. Clamping end to start.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [11–22], lower_priority='Action_PullLeadBlock' annotated_start=14, effective_Action_PullLeadBlock_start=23.
> - Action 'Action_None' range [11-45] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-50] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-44] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-57] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [14-50] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-100] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [28-35] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-92] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [14-31] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [59-95] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-57] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [23-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [32-53] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [67-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [99-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-9] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-27] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-59] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-120] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-44] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-45] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-46] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-57] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-62] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-120] for track '28' has 2 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.