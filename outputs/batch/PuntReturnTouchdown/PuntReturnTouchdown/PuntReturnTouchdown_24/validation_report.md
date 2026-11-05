# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_24`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 53 |
| Player Tracks | 53 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 213 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 50: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [8-353] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-134] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-187] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-223] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-310] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-365] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-465] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-474] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-233] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-151] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-173] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-248] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-410] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [413-422] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-510] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-81] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-133] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-84] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-147] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-221] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-256] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-319] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-44] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-66] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-136] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-160] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-129] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-145] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-248] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-265] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-137] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-159] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-168] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-193] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-240] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-14] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-43] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-216] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-425] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-105] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-161] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-222] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-267] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-306] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-375] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-185] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-251] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-327] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-347] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-390] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-196] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-298] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [303-424] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [426-480] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-506] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-534] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-211] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-252] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-396] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [399-404] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-423] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [427-490] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [492-530] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [226-348] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-195] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-288] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [295-349] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-220] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-286] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-259] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-491] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-372] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-455] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-308] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-329] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-411] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [244-255] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-383] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-347] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [366-479] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [482-493] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-497] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-511] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-324] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-355] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-430] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-495] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [336-357] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-348] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-352] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-409] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-420] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [422-423] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-514] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-364] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-462] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-460] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-440] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-461] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [471-479] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-539] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-539] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-528] for track '52' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.