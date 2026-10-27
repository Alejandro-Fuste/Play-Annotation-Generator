# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_346`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_346/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '3' (RG) duration 96 frames exceeds threshold 90 frames [start=24, end=119].
> - Validation warning: Action 'Action_DownBlock' for track '10' (RT) duration 96 frames exceeds threshold 90 frames [start=24, end=119].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [21–34], lower_priority='Action_DownBlock' annotated_start=24, effective_Action_DownBlock_start=35.
> - Action 'Action_None' range [21-56] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [44-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [24-67] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [69-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-39] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [33-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-194] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-207] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [24-50] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [55-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [24-78] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [81-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [35-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [40-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [47-51] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [72-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [99-107] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-210] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-143] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-170] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.