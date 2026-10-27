# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_128`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_128/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [28–42], lower_priority='Action_DownBlock' annotated_start=30, effective_Action_DownBlock_start=43.
> - Action 'Action_PullLeadBlock' range [30-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-206] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-161] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-107] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [77-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [199-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [43-65] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [68-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-57] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-168] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [51-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [30-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-121] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-154] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-196] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-176] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-177] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.