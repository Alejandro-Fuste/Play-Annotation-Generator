# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_91`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 58 |
| Player Tracks | 58 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 252 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Segment 'Action_CatchKick' for track '25' has invalid range: start=214, end=189. Clamping end to start.
> - Segment 'Action_CrossGoalLine' for track '25' has invalid range: start=588, end=409. Clamping end to start.
> - Action 'Action_None' range [16-348] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-364] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-504] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [508-524] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-377] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-384] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-402] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-554] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [569-577] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-599] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-325] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-425] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [427-451] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [453-455] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-465] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-471] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-503] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-511] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-529] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [534-564] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [569-572] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-595] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-515] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [518-558] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [566-596] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [16-175] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [177-277] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-446] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [451-462] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [464-487] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [495-497] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-500] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-352] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [16-67] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-366] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [368-373] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-385] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [387-409] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-416] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-300] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-483] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [485-491] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-511] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [514-518] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-540] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [555-562] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [564-565] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-581] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-599] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-197] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-277] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-254] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-211] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-421] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [423-506] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [509-526] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [528-542] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [544-569] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-581] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [585-593] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-132] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-443] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [448-503] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [505-506] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-518] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-595] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [16-501] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [504-599] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-333] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-221] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-193] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-27] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-193] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-415] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [419-427] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-439] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-233] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-271] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-291] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-374] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [376-444] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [455-456] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-465] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-469] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-474] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-491] for track '19' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [495-528] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [530-544] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [546-560] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-599] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-181] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-193] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-451] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [455-458] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-493] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [495-599] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-245] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-356] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [359-409] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-275] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-290] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-335] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-292] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-326] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-455] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [461-471] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-491] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [493-504] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-512] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [514-517] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-522] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-540] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [544-545] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-548] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-555] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-570] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-506] for track '31' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [513-566] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-576] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [578-579] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-592] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-560] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [562-566] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-599] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [301-325] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-504] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-514] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-403] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-431] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-439] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [445-446] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-474] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-483] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-489] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-496] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-505] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-376] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-412] for track '37' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [426-427] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-432] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-353] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-386] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-404] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-407] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-385] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-393] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-401] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-410] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-410] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [412-416] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [430-448] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-449] for track '46' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [462-470] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-485] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-500] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [504-514] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [470-480] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-484] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-517] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [520-521] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-536] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-590] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [479-499] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [502-503] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-506] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-523] for track '48' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [525-538] for track '48' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [540-541] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-548] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-491] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [505-513] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [517-522] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [530-534] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [536-538] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-552] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-565] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-486] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-495] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [498-499] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-514] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-526] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-547] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [560-585] for track '50' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [516-520] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-524] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-552] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-563] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-568] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [570-571] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-580] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-582] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [586-589] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-590] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [593-598] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [591-597] for track '57' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.