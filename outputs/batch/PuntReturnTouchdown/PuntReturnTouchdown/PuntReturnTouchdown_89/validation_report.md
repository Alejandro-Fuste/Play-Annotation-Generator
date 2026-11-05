# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_89`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 63 |
| Player Tracks | 63 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 205 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 701 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 701 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [36-272] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-279] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-329] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-644] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [649-650] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-181] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-168] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-309] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-268] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-283] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-301] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-327] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-307] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-701] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-191] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-250] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-85] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-257] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-228] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-275] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-283] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-305] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-314] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [36-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [36-58] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-284] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-392] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [412-618] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-110] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-153] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [155-177] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-345] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-655] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-282] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-156] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-159] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-267] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-300] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-148] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-324] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [338-342] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [226-265] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [272-301] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [304-305] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [318-653] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-188] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-337] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-266] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-399] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-404] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-575] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-235] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-254] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-663] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-313] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-340] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [292-701] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-315] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-343] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-317] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-608] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [610-612] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [622-670] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-346] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-362] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-694] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-345] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-675] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-345] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-690] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-352] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-375] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-379] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-349] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-472] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-494] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-354] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-377] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-432] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-440] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-497] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [357-362] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-377] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-578] for track '49' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-373] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-663] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-494] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-500] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-512] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-437] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-455] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-658] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-374] for track '53' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [385-401] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-407] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-426] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-434] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-446] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [451-458] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [461-464] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-472] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-482] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-491] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [516-520] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-538] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-556] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-564] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [594-605] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [615-616] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-375] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-383] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-622] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-405] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-664] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [431-433] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-460] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-547] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-628] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [634-648] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [650-656] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [658-665] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [667-683] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [694-695] for track '62' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.