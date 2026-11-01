# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_47`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 218 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [153–167], lower_priority='Action_ZoneBlock' annotated_start=155, effective_Action_ZoneBlock_start=168.
> - Action 'Action_None' range [153-337] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-335] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-352] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-378] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [381-434] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [153-319] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-434] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-313] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-318] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-379] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [381-393] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-397] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-213] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-311] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-326] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-339] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-360] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-385] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-393] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-418] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-349] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-367] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-370] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-385] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-392] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-409] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-302] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-313] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-332] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-424] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-441] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-449] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-223] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-226] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-37] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-54] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-100] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-135] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-149] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 153, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [153-158] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [153-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [205-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [211-213] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [215-220] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [225-229] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-257] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-277] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-296] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-303] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-200] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-242] for track '14' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-53] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-88] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-126] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-17] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [211-213] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [215-233] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [237-238] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [204-213] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [215-217] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [225-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-260] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-293] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-305] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-358] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-362] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-367] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-375] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-394] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-17] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-154] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-100] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-197] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-212] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-257] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-270] for track '23' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-296] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-219] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [232-305] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [310-349] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [355-358] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [360-363] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [365-390] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [392-411] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-297] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-302] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [341-344] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-290] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-306] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-402] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [410-412] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-419] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-443] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-447] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-296] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-332] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-349] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-336] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-339] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-361] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-379] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-387] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-402] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-424] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [429-434] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-359] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-449] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [362-385] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-392] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-419] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-379] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-425] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-440] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [445-449] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-392] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-424] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-385] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-400] for track '41' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.