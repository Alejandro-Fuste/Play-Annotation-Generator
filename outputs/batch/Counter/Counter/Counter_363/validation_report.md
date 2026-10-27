# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_363`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_363/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 155 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 130 frames exceeds threshold 90 frames [start=85, end=214].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [82–98], lower_priority='Action_DownBlock' annotated_start=85, effective_Action_DownBlock_start=99.
> - Validation warning: Action 'Action_PullBlock' for track '19' (LG) duration 130 frames exceeds threshold 90 frames [start=85, end=214].
> - Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 130 frames exceeds threshold 90 frames [start=85, end=214].
> - Validation warning: Action 'Action_DownBlock' for track '21' (RT) duration 130 frames exceeds threshold 90 frames [start=85, end=214].
> - Action 'Action_None' range [82-135] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [95-141] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [143-214] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-250] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-181] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [186-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-193] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-246] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-255] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-188] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-219] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-154] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-299] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-174] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-190] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-198] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-293] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-292] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [99-159] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [161-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-265] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-294] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [85-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [158-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [201-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-223] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [85-214] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [85-124] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-299] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-81] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-53] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-71] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-94] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-126] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-189] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-140] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-165] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-223] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-176] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-221] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-281] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-267] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '39' has 1 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.