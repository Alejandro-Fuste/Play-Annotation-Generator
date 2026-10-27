# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_77`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_77/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [74–87], lower_priority='Action_DownBlock' annotated_start=77, effective_Action_DownBlock_start=88.
> - Action 'Action_None' range [74-164] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-173] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-113] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-135] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-258] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [77-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [132-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-234] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-251] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-236] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-149] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-229] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-238] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [250-254] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [257-259] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-237] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [240-243] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-269] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-136] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-152] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-221] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-236] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-109] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-261] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [77-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-221] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-152] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-174] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-248] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-260] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [77-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-216] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-269] for track '27' has 3 frames without a visible bounding box.
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