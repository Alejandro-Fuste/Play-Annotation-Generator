# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_223`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_223/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 448: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '10' has invalid range: start=84, end=77. Clamping end to start.
> - Validation warning: Action 'Action_DownBlock' for track '12' (RT) duration 103 frames exceeds threshold 90 frames [start=35, end=137].
> - Validation warning: Action 'Action_DownBlock' for track '20' (C) duration 103 frames exceeds threshold 90 frames [start=35, end=137].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [32–48], lower_priority='Action_DownBlock' annotated_start=35, effective_Action_DownBlock_start=49.
> - Action 'Action_None' range [32-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-129] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-128] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-92] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [35-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [38-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-184] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [35-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-100] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-61] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-91] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-105] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-148] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-214] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-238] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-191] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-166] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-191] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-221] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-232] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-191] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '42' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.