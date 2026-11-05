# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_74`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_74/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 62 |
| Player Tracks | 62 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 281 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 659 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [45-64] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-70] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-104] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-197] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-296] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-349] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-366] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-377] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-432] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-447] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [450-452] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-224] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-312] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-426] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [429-434] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-453] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [458-459] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-400] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-438] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-467] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [471-483] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-491] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-500] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [502-503] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-511] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [517-523] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [526-527] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-557] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [616-617] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [637-640] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [647-659] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-382] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-463] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-482] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-491] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-71] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-237] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-273] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-289] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-306] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-327] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-349] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-256] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-377] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [380-387] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-395] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-406] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-416] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-426] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-270] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [273-377] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-397] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [407-409] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-416] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-453] for track '9' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [458-461] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-93] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [99-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-290] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-330] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-419] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [426-444] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [446-447] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-457] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-80] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-316] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-228] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-302] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-360] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-379] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-399] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [411-432] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [452-453] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-82] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-189] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-201] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-361] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [370-375] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-397] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [402-417] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [419-432] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [442-445] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-459] for track '16' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [474-476] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-186] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-250] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-407] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [411-415] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-432] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-447] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [498-518] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [123-331] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-196] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-206] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-310] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-370] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-395] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-408] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-417] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-431] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [443-444] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-261] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-325] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-387] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-420] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [424-434] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-444] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-238] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-273] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-339] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [346-393] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-379] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-388] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-535] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [538-541] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [582-591] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [601-659] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-216] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-261] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-298] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-310] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-384] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [386-397] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [402-407] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [411-462] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-338] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-397] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-422] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [428-433] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-438] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-455] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [458-461] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [514-519] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-523] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-532] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-553] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-373] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-517] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [522-523] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-532] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [535-577] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [582-616] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [619-623] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [627-639] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [641-642] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [648-659] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-293] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-314] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-338] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-348] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-430] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-321] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-659] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-360] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-374] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-553] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [556-559] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [574-578] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-587] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-625] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [658-659] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-368] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-372] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-417] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [421-438] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [433-446] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [449-453] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-468] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-444] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-457] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-461] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-474] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [484-504] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-609] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [613-625] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-527] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-533] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-541] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-557] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-510] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-519] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [527-543] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-552] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [552-554] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [572-573] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-578] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [586-594] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-659] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-631] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [633-635] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [637-639] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [594-596] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [608-638] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [645-647] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-659] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [613-616] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_CrossGoalLine' range [630-633] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [637-645] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [647-652] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [618-630] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [637-645] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [619-621] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-630] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [632-645] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [625-627] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [641-645] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [649-659] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [644-645] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [646-647] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [650-657] for track '58' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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