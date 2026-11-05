# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_85`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 62 |
| Player Tracks | 62 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 267 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [30-63] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-629] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-144] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-305] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [309-629] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-383] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-413] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-378] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-58] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-145] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-605] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [612-613] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-618] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-176] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-203] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-318] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-461] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [465-565] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-604] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-365] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [368-374] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-380] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-476] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [478-481] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-623] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-111] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-317] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-359] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-404] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-418] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [421-494] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [496-572] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [582-629] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-460] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [469-473] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-497] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [499-501] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-504] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-617] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [624-628] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-61] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-300] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-307] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-362] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-367] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-377] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-394] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-404] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-410] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-463] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [467-480] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-495] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [30-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-26] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-88] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-628] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-191] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-138] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-309] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [311-315] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-153] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-273] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-280] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-337] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-370] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-225] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-271] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-351] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-365] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-392] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-404] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-272] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-296] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-263] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [265-288] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-377] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-384] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-462] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-272] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [273-371] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [373-383] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-436] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-450] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-457] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-466] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-472] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-242] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-251] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-438] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-629] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-402] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-352] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-405] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-412] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-426] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-440] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-444] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-448] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-471] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-476] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-483] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-503] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-510] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-541] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [549-550] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-421] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-427] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [429-446] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [449-453] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [460-472] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [478-481] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [491-552] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [559-561] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [563-564] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [566-575] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [577-578] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_CrossGoalLine' for track '35' starts at frame 609, but the player has no visible bounding box on this frame.
> - Action 'Action_CrossGoalLine' range [609-609] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_CrossGoalLine' range [612-619] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-623] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-629] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-422] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-424] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-429] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-494] for track '39' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [496-502] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-510] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-516] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-606] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-485] for track '40' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [488-552] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [554-560] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-586] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-596] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [602-623] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-449] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-452] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-461] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [463-484] for track '43' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [490-503] for track '43' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [519-520] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-526] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-535] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [554-629] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-454] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-459] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-519] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-565] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [571-572] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [602-603] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-470] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-479] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-485] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-494] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-499] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-516] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-536] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [545-547] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-552] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [498-526] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [529-541] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-568] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [537-549] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-629] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-542] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-567] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-572] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-570] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-574] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-586] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [571-576] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-580] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [572-575] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-588] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-583] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-586] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-597] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [600-601] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [603-623] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [626-628] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [601-602] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-606] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-618] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-616] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-616] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [626-629] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-622] for track '61' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.