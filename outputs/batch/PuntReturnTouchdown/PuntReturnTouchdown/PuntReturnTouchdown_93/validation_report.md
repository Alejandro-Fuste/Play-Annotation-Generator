# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_93`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 73 |
| Player Tracks | 73 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 221 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 188: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_CrossGoalLine' for track '7' has invalid range: start=564, end=206. Clamping end to start.
> - Action 'Action_None' range [98-245] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-413] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [415-479] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-569] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-169] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-189] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-184] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-236] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-308] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-322] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-215] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-313] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-206] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-192] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-214] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-177] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [98-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [120-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-213] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-235] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-246] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [284-358] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-231] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-262] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [264-283] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-361] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-454] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-211] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-250] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-270] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-231] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-247] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-334] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-342] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-348] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-355] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-367] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-393] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-411] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-313] for track '34' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [317-363] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [252-256] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-274] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-292] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-307] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-442] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-295] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-315] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-331] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-569] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-291] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-303] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-314] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-397] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-293] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-400] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-337] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-367] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-382] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-412] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-333] for track '47' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [341-356] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [378-402] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-319] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-325] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-356] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-315] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-342] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-357] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-384] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-396] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-468] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [471-473] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-483] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-372] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-395] for track '51' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-342] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-391] for track '53' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [394-396] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-329] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-346] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-569] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-339] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-405] for track '58' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [408-455] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-342] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-374] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-363] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-393] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-569] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-394] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-367] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-377] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [380-437] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [366-371] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-452] for track '64' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-497] for track '65' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [500-502] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-396] for track '66' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [403-542] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-390] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-400] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-455] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-568] for track '69' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [405-407] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-428] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-446] for track '70' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [456-503] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-555] for track '71' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [563-566] for track '71' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [473-549] for track '72' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [551-559] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-567] for track '72' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.
> - Player track '67' has undefined position. Will map to Position_Unknown.
> - Player track '67' has undefined team_side. Will map to Team_Unknown.
> - Player track '68' has undefined position. Will map to Position_Unknown.
> - Player track '68' has undefined team_side. Will map to Team_Unknown.
> - Player track '69' has undefined position. Will map to Position_Unknown.
> - Player track '69' has undefined team_side. Will map to Team_Unknown.
> - Player track '70' has undefined position. Will map to Position_Unknown.
> - Player track '70' has undefined team_side. Will map to Team_Unknown.
> - Player track '71' has undefined position. Will map to Position_Unknown.
> - Player track '71' has undefined team_side. Will map to Team_Unknown.
> - Player track '72' has undefined position. Will map to Position_Unknown.
> - Player track '72' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.