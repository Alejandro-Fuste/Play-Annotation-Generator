# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_294`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_294/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [17–33], lower_priority='Action_DownBlock' annotated_start=20, effective_Action_DownBlock_start=34.
> - Action 'Action_PullBlock' range [20-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-184] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-254] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-45] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-95] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [20-51] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [53-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-169] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-58] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [20-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-251] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-260] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-248] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-267] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [20-105] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-133] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [29-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [58-174] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [34-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [40-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-44] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-39] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-119] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-44] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-96] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-261] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-269] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-269] for track '35' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.