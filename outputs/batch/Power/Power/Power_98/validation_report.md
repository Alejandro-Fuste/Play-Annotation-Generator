# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_98`
- **Input XML**: `outputs/batch/Power/Power/Power_98/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 53 |
| Player Tracks | 53 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 164 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 198: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action 'Action_PreSnap' range [29-386] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [246-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [270-282] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-86] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-304] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-320] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-417] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-304] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-381] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-444] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-135] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-337] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-263] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-272] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-374] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [439-486] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-244] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-320] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-369] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-458] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-486] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-531] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-542] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-249] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-350] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-396] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [411-412] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-236] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-324] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-439] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [450-472] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-549] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [555-560] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-47] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-130] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-162] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-198] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-207] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-227] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-238] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-256] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-79] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-234] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [252-281] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-312] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-373] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-414] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-254] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-300] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-355] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-392] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-413] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-260] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-264] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-274] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-292] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-304] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-384] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-292] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-279] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-321] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-337] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-352] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-362] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-420] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-378] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-419] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [424-430] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [451-452] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [455-457] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [459-485] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [531-533] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [543-544] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-292] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-378] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-367] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-370] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-374] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-386] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-397] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [426-429] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [431-469] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-343] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-362] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-376] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-304] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-331] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-400] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-383] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-314] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-321] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-326] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-337] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-326] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-346] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-355] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-373] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-384] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-407] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-456] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-366] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-373] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-381] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-391] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-409] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-420] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-370] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-370] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-373] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-376] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-376] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-386] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [392-420] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-383] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-392] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-399] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-403] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-424] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-381] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-384] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-392] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-543] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [392-399] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-403] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-410] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [477-484] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-426] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [413-434] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [440-452] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [464-467] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [455-479] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [485-499] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [507-569] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [463-469] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [471-509] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [472-473] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [478-490] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [493-522] for track '51' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.