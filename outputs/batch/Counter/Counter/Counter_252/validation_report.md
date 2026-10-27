# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_252`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_252/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [45–60], lower_priority='Action_DownBlock' annotated_start=48, effective_Action_DownBlock_start=61.
> - Action 'Action_None' range [45-56] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-113] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [48-77] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [48-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-199] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-187] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-86] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [48-67] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [75-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [113-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-63] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-82] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-136] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [48-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [74-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [77-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [45-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [68-72] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [84-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-192] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-55] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-88] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-192] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-150] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.