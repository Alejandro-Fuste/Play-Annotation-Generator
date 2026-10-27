# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_66`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 44 |
| Ball Tracks | 3 |
| CSV events parsed | 19 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '13' (LG) duration 99 frames exceeds threshold 90 frames [start=170, end=268].
> - Action 'Action_None' range [168-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-435] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-269] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [170-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [205-206] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-75] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [170-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [228-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-437] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-254] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-226] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-258] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [170-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [184-199] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [231-246] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-325] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-167] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-284] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-334] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-328] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-186] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-479] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-267] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-315] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-33] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-236] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [238-307] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-479] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-287] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-297] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-311] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-309] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-280] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-306] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-473] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-479] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-329] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-372] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-319] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-387] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-432] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [433-434] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-461] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-474] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-434] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-466] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-438] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-447] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-447] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-453] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-470] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-451] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-479] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [471-472] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-475] for track '46' has 1 frames without a visible bounding box.
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
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.