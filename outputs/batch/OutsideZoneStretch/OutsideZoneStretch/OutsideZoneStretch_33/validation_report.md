# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_33`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 102 |
| Player Tracks | 102 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 259 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 68: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [0-392] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-392] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-342] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-413] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-397] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-129] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-367] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-137] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-382] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-411] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-356] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-241] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-123] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-355] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-351] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-74] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-115] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [128-227] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-373] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-53] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-413] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-389] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-397] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-245] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-396] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-378] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-419] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-346] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-351] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-166] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-194] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-369] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-247] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-276] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-325] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-335] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-339] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-258] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-278] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-304] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-258] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-275] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-309] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-381] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-290] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-352] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-272] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-276] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-339] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-289] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-270] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-290] for track '36' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-340] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-308] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-317] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-325] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-328] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-333] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-271] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-275] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-277] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-311] for track '39' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-279] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-357] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-361] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-284] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-302] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-327] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-366] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-276] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-295] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-348] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-356] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-279] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-285] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-308] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-352] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-302] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-308] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-286] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-305] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-339] for track '47' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-345] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-349] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-289] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-307] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-350] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-294] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-307] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-322] for track '49' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-337] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-295] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-308] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-321] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-329] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-324] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-335] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-304] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-345] for track '52' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-349] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-304] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-318] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-326] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-330] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-344] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-347] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-353] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-330] for track '54' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-357] for track '54' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-304] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-326] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-330] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-333] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-338] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-343] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-307] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-314] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-322] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-327] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-334] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-370] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-320] for track '58' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-311] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-329] for track '59' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-337] for track '59' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-343] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-352] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-334] for track '60' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-318] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-318] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-318] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-332] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-325] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-337] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-343] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-348] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-332] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-332] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-339] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-352] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-349] for track '68' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-379] for track '68' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-384] for track '68' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-389] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-395] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-398] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-403] for track '68' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-337] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-342] for track '70' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-342] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-360] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-342] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-375] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-352] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-358] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-375] for track '74' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-381] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-357] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-365] for track '76' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-396] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-400] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-411] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-399] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-407] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-410] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [413-416] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-387] for track '78' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-396] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-411] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-391] for track '79' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-385] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-369] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-390] for track '82' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-371] for track '83' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-390] for track '84' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-373] for track '85' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-393] for track '86' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-399] for track '86' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-375] for track '87' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-382] for track '87' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-389] for track '87' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-397] for track '88' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-377] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-382] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-385] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-378] for track '90' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-409] for track '90' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-385] for track '91' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-400] for track '91' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-405] for track '91' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-419] for track '91' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-407] for track '92' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-389] for track '93' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-394] for track '93' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-381] for track '94' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-381] for track '95' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-388] for track '95' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-381] for track '96' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-385] for track '96' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-381] for track '97' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [392-395] for track '98' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-401] for track '99' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-405] for track '99' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-407] for track '100' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '73' has undefined position. Will map to Position_Unknown.
> - Player track '73' has undefined team_side. Will map to Team_Unknown.
> - Player track '74' has undefined position. Will map to Position_Unknown.
> - Player track '74' has undefined team_side. Will map to Team_Unknown.
> - Player track '75' has undefined position. Will map to Position_Unknown.
> - Player track '75' has undefined team_side. Will map to Team_Unknown.
> - Player track '76' has undefined position. Will map to Position_Unknown.
> - Player track '76' has undefined team_side. Will map to Team_Unknown.
> - Player track '77' has undefined position. Will map to Position_Unknown.
> - Player track '77' has undefined team_side. Will map to Team_Unknown.
> - Player track '78' has undefined position. Will map to Position_Unknown.
> - Player track '78' has undefined team_side. Will map to Team_Unknown.
> - Player track '79' has undefined position. Will map to Position_Unknown.
> - Player track '79' has undefined team_side. Will map to Team_Unknown.
> - Player track '80' has undefined position. Will map to Position_Unknown.
> - Player track '80' has undefined team_side. Will map to Team_Unknown.
> - Player track '81' has undefined position. Will map to Position_Unknown.
> - Player track '81' has undefined team_side. Will map to Team_Unknown.
> - Player track '82' has undefined position. Will map to Position_Unknown.
> - Player track '82' has undefined team_side. Will map to Team_Unknown.
> - Player track '83' has undefined position. Will map to Position_Unknown.
> - Player track '83' has undefined team_side. Will map to Team_Unknown.
> - Player track '84' has undefined position. Will map to Position_Unknown.
> - Player track '84' has undefined team_side. Will map to Team_Unknown.
> - Player track '85' has undefined position. Will map to Position_Unknown.
> - Player track '85' has undefined team_side. Will map to Team_Unknown.
> - Player track '86' has undefined position. Will map to Position_Unknown.
> - Player track '86' has undefined team_side. Will map to Team_Unknown.
> - Player track '87' has undefined position. Will map to Position_Unknown.
> - Player track '87' has undefined team_side. Will map to Team_Unknown.
> - Player track '88' has undefined position. Will map to Position_Unknown.
> - Player track '88' has undefined team_side. Will map to Team_Unknown.
> - Player track '89' has undefined position. Will map to Position_Unknown.
> - Player track '89' has undefined team_side. Will map to Team_Unknown.
> - Player track '90' has undefined position. Will map to Position_Unknown.
> - Player track '90' has undefined team_side. Will map to Team_Unknown.
> - Player track '91' has undefined position. Will map to Position_Unknown.
> - Player track '91' has undefined team_side. Will map to Team_Unknown.
> - Player track '92' has undefined position. Will map to Position_Unknown.
> - Player track '92' has undefined team_side. Will map to Team_Unknown.
> - Player track '93' has undefined position. Will map to Position_Unknown.
> - Player track '93' has undefined team_side. Will map to Team_Unknown.
> - Player track '94' has undefined position. Will map to Position_Unknown.
> - Player track '94' has undefined team_side. Will map to Team_Unknown.
> - Player track '95' has undefined position. Will map to Position_Unknown.
> - Player track '95' has undefined team_side. Will map to Team_Unknown.
> - Player track '96' has undefined position. Will map to Position_Unknown.
> - Player track '96' has undefined team_side. Will map to Team_Unknown.
> - Player track '97' has undefined position. Will map to Position_Unknown.
> - Player track '97' has undefined team_side. Will map to Team_Unknown.
> - Player track '98' has undefined position. Will map to Position_Unknown.
> - Player track '98' has undefined team_side. Will map to Team_Unknown.
> - Player track '99' has undefined position. Will map to Position_Unknown.
> - Player track '99' has undefined team_side. Will map to Team_Unknown.
> - Player track '100' has undefined position. Will map to Position_Unknown.
> - Player track '100' has undefined team_side. Will map to Team_Unknown.
> - Player track '101' has undefined position. Will map to Position_Unknown.
> - Player track '101' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.