# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_34`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '1' (LG) duration 91 frames exceeds threshold 90 frames [start=65, end=155].
> - Overlapping action conflict at frame 73 for track '4': 'Action_SnapReceive' vs 'Action_Handoff'. Overriding with 'Action_Handoff'.
> - Validation warning: Action 'Action_DownBlock' for track '5' (RT) duration 91 frames exceeds threshold 90 frames [start=65, end=155].
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [60–73], lower_priority='Action_DownBlock' annotated_start=65, effective_Action_DownBlock_start=74.
> - Action 'Action_None' range [60-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [65-112] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-169] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-141] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [156-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-135] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [74-84] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-143] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [68-116] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-105] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-135] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-155] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-217] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-204] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-145] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-136] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-144] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-215] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-239] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-206] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.