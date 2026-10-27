# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_151`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_151/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 220 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 304: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_None' range [213-263] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-300] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-305] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-449] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-245] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-274] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-300] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-252] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [256-334] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [350-360] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [396-425] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-297] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-297] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-229] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-274] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-288] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-443] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-447] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-243] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-274] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-304] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-449] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-222] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-246] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-275] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-301] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-316] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-13] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-188] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [218-219] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [230-244] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [254-272] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [281-290] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-425] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [433-444] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-12] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-265] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-14] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-146] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-231] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-188] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-201] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-213] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [218-221] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [226-301] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [303-306] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-217] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [218-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [226-267] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 213, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [213-213] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-290] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-357] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [366-377] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [218-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [230-251] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [254-291] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [293-294] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-78] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-188] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-201] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 213, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [213-213] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-244] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-289] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-298] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-388] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-400] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-413] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [425-449] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-186] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-201] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' for track '20' starts at frame 213, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [213-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-114] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-201] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [213-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [226-231] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [234-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-274] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-338] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-376] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-352] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-331] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-389] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-446] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-324] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-365] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-370] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-333] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-337] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-347] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-357] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-376] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-449] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-348] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-354] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-449] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-351] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-359] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [363-366] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-360] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-398] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-377] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-400] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-413] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [415-419] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-434] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-447] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-398] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [401-429] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [431-446] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-394] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-402] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-412] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-422] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-431] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-436] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-449] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [401-405] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-412] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-421] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-447] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-411] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-446] for track '46' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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