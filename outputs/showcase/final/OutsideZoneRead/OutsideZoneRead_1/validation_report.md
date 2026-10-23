# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_1`
- **Input XML**: `output_showcase_final/OutsideZoneRead/OutsideZoneRead_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 144 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 3: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 3: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [3-368] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [371-377] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-410] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-419] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-334] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-340] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-353] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-358] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-257] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-212] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-242] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-257] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-267] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-272] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-277] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-407] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [220-227] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-247] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-377] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-396] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-406] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-417] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-335] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-391] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [393-407] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-257] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-389] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-340] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-356] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-370] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-377] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-385] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [417-418] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [199-202] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [208-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [216-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-284] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-281] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-316] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-328] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-393] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-401] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-409] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-110] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-195] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-248] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-257] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-275] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-325] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-248] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-258] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-99] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-113] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-242] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-257] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-306] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-198] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-193] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-197] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-100] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-196] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-242] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-419] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-227] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-319] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-335] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-297] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-326] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-370] for track '25' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-377] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-298] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-317] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-338] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-383] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [385-395] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-405] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-419] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-352] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-362] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-366] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-379] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-419] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-362] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-391] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-399] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-418] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-363] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-373] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-383] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-366] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [385-387] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-393] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-403] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-410] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-419] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-393] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-404] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [410-411] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-396] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-419] for track '40' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.