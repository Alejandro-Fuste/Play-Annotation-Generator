# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneStretch_5`
- **Input XML**: `outputs/batch/InsideZoneStretch/InsideZoneStretch/InsideZoneStretch_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 199 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 12: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 12: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_None' range [146-361] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-419] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-316] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-338] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [340-360] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [362-369] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-375] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-383] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-390] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-399] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-404] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-416] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-216] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-309] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-344] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-216] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-231] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-260] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [146-185] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-283] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-328] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-338] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-343] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-386] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [192-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-213] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-320] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-327] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-374] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [385-387] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-257] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-290] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-297] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-155] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-316] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-360] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [365-368] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-374] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-382] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-390] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-397] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-187] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-245] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-329] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-419] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-312] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-331] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [335-393] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [396-397] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-411] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [180-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [165-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-245] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-316] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-322] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-342] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-351] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-14] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-22] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-158] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '19' starts at frame 159, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [159-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [161-195] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-237] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-255] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-270] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-278] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-316] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-419] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [177-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-333] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [335-338] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-343] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-419] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-17] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-31] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-176] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-332] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-188] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-237] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-247] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-278] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-233] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-242] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-352] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-387] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-410] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-242] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-281] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [223-242] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-359] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-379] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [383-386] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-244] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-258] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-329] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-316] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [318-388] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [390-395] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-267] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-388] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-322] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-343] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-305] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [308-330] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-346] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-299] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-329] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [341-355] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [358-419] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-312] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-325] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-334] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-419] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-318] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-419] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-399] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-419] for track '41' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.