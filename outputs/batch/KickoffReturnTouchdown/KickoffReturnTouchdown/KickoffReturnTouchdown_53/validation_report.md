# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_53`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 166 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 108: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Segment 'Action_CatchKick' for track '29' has invalid range: start=246, end=211. Clamping end to start.
> - Action 'Action_None' range [15-220] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-403] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [405-464] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [466-470] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-482] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [494-629] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-240] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-354] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [356-627] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-457] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-192] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-566] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [569-571] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [578-579] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-625] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-174] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-429] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [432-449] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [466-471] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-478] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-627] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-183] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-224] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-249] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-275] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-297] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-375] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-234] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-233] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-399] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-181] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-91] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-198] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-629] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-242] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-507] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-563] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [571-627] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-629] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [15-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-82] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-92] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-107] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-241] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [248-266] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-272] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-341] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [346-371] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [373-488] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [492-563] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [565-629] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-164] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [167-454] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-458] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-470] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-629] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-21] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-264] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-309] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-364] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-429] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-491] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [494-496] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-536] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-621] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [623-627] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-58] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-67] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-183] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-218] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-232] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-387] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-397] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-416] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-330] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-344] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-508] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [513-603] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [608-609] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-614] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [625-627] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-223] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-520] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [543-545] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-594] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-270] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-250] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-288] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-412] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-419] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-426] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-368] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [370-441] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [447-454] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [476-477] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [481-620] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-308] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-522] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [431-453] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [455-456] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-464] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [467-474] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [465-629] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-505] for track '36' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.