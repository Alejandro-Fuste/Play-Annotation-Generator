# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_106`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 215 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [13-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-424] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-512] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [516-519] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-207] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-256] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-321] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [328-360] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-394] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-493] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-562] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-235] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-267] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-273] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [13-171] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [219-267] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-319] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-324] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-489] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-554] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [556-598] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-629] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [13-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-149] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-261] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-287] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-295] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-312] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-361] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-408] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-513] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [516-614] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-490] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [493-615] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [618-620] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [622-629] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-128] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-207] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-139] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-436] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [439-501] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-554] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-588] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [595-608] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-618] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [625-629] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-358] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-220] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [246-248] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [277-544] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [556-567] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [571-574] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [580-582] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [584-586] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [590-593] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [613-614] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-121] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-151] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-190] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-213] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-458] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [464-494] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-570] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-618] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-35] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-90] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-478] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [481-548] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-567] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [572-574] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-582] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [596-600] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-395] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [404-441] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [443-499] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [502-545] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-140] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-276] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-465] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [487-552] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-598] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [601-606] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-227] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-265] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-281] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-403] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-256] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-311] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-276] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-327] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-477] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [480-608] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-617] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-346] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [349-428] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [430-446] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-284] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-610] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [613-617] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-273] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-532] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [538-540] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-570] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-383] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [390-528] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-436] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-322] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-515] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-535] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [539-622] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [308-390] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-443] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-459] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-535] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-555] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-578] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [583-589] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-388] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-420] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-481] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [373-397] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-429] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-608] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [614-629] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-628] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [461-513] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [518-520] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [530-542] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [544-551] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [555-574] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [577-580] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [592-594] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_CrossGoalLine' range [599-600] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-626] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [462-544] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [483-522] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [527-536] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-569] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-506] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-521] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-530] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-549] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-558] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-569] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-580] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [583-584] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [593-599] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-526] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [529-530] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [537-542] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [577-579] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [527-544] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-568] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [573-593] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [595-606] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [617-629] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [599-600] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [603-605] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-624] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-622] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [625-626] for track '44' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.