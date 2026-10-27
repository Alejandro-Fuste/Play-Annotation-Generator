# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_23`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 48: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '0' (WR2) duration 106 frames exceeds threshold 90 frames [start=113, end=218].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [103–116], lower_priority='Action_DownBlock' annotated_start=113, effective_Action_DownBlock_start=117.
> - Action 'Action_None' range [103-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-224] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-273] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [147-168] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [177-286] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [291-294] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-174] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-221] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-297] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-287] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [103-116] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-231] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-269] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-294] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-127] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-231] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-187] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-277] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [113-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [117-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [135-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [190-195] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-231] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-294] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [138-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-4] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-75] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-108] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-277] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-297] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-211] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-231] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-192] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-286] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-231] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-213] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-266] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-293] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-290] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-231] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-288] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-258] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.