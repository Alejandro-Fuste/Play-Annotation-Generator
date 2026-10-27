# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_319`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_319/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '8' (RG) duration 103 frames exceeds threshold 90 frames [start=101, end=203].
> - Validation warning: Action 'Action_DownBlock' for track '20' (LG) duration 103 frames exceeds threshold 90 frames [start=101, end=203].
> - Validation warning: Action 'Action_DownBlock' for track '21' (C) duration 103 frames exceeds threshold 90 frames [start=101, end=203].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [98–108], lower_priority='Action_DownBlock' annotated_start=101, effective_Action_DownBlock_start=109.
> - Action 'Action_None' range [98-278] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-287] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-265] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-295] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-263] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-279] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-289] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-263] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-195] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-207] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-272] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-299] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-241] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-293] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-293] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [101-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [138-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-175] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-192] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-220] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-234] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-272] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [131-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-270] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [101-133] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [137-144] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [146-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-283] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [109-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [155-203] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-274] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-281] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-296] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-271] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-290] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-275] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-281] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-276] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-285] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-293] for track '29' has 2 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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