# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_97`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 83 |
| Player Tracks | 83 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 251 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 195: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
> - Row 196: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 196: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 196: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [13-238] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-319] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-38] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-255] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-43] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-354] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-33] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-291] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-320] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-326] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-592] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [13-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-287] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-298] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-465] for track '6' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [470-592] for track '6' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [594-597] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [602-629] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-437] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-448] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-468] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-472] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-197] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-212] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-310] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-334] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-442] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-448] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-537] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-582] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [13-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-236] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-266] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-272] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-261] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-15] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-18] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-38] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-158] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [161-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-267] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-127] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-139] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-157] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-137] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-167] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-481] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [485-525] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [527-592] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [594-603] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-211] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-182] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [228-266] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [270-307] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-199] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-319] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-273] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-310] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-244] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-267] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-251] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-469] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-474] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-507] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-559] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [563-565] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-267] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-314] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-440] for track '41' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [263-271] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-343] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-321] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-326] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-566] for track '44' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [569-588] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-629] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-310] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-598] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-304] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-444] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-506] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [508-629] for track '46' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [293-441] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [444-492] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-579] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [584-585] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-557] for track '49' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [559-572] for track '49' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [576-582] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [585-587] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-318] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-564] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-578] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [583-588] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [593-600] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-326] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-336] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-418] for track '51' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [432-454] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-334] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-469] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [471-578] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-604] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-426] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-494] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-499] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-502] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-556] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-585] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-592] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [594-599] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-583] for track '54' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [586-588] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [595-597] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [614-616] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-629] for track '55' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [358-383] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-375] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-398] for track '58' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [382-393] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-432] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-457] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [468-552] for track '60' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-409] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-425] for track '61' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [428-575] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [579-580] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-592] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [594-596] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-434] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-447] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-452] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-606] for track '64' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [485-628] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-629] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-500] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [502-503] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-518] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-503] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-510] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-573] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-576] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-626] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-629] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-548] for track '70' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [520-521] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-523] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-537] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-558] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-573] for track '75' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [569-571] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [591-592] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-597] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [613-615] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [593-599] for track '78' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [602-611] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-618] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [616-618] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-625] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [622-625] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-629] for track '82' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.