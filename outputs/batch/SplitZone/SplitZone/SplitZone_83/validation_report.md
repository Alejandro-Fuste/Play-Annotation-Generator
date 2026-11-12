# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_83`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 133 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_SplitBlock' for track '4' has invalid range: start=86, end=79. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 130 frames exceeds threshold 90 frames [start=83, end=212].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [80–94], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=95.
> - Validation warning: Action 'Action_ZoneBlock' for track '22' (RG) duration 98 frames exceeds threshold 90 frames [start=83, end=180].
> - Action 'Action_None' range [95-253] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-133] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-238] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-280] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-133] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [80-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [105-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-146] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-181] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-299] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-299] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [174-181] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-98] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [80-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [131-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-27] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-110] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-189] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-149] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-177] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [179-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-119] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-159] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-176] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-216] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-186] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-151] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-269] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-273] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-250] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-269] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-278] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-200] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-226] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-281] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-278] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-242] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-273] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-288] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-268] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '44' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.