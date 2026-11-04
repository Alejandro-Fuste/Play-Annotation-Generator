# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_38`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 73 |
| Player Tracks | 73 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 243 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 659 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 78: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
> - Segment 'Action_CrossGoalLine' for track '19' has invalid range: start=651, end=553. Clamping end to start.
> - Action 'Action_None' range [13-300] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-659] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-223] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-289] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-296] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-319] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-616] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-297] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-274] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-318] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-313] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-241] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-371] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-423] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-330] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-204] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-305] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [312-319] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-302] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-372] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-455] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-464] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [466-469] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-472] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-475] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-481] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-342] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-411] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-659] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-226] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-257] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-263] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-283] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-599] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [13-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-243] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-52] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-171] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_CatchKick' range [187-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 200, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [200-205] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [206-215] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [233-293] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [305-553] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-220] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-298] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-381] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-567] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-586] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-262] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-325] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-121] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-308] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-317] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-298] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-364] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-540] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-649] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-306] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-287] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-300] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-312] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-352] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-304] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-384] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-569] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-585] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-384] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [386-573] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-581] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-588] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [600-652] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-338] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-386] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-568] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-374] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-378] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-352] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-363] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-659] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-367] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-372] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-499] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [502-606] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-405] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-408] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-411] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-417] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-560] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [435-512] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-573] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-533] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-498] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-509] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-520] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [523-525] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-532] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-543] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [552-556] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-509] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-514] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-519] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-524] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [526-529] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [531-534] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [537-540] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [550-551] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-562] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [571-572] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-582] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-587] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [589-590] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [615-620] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [622-643] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [513-529] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [533-534] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [537-541] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [550-551] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-518] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-541] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [630-634] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-543] for track '54' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [547-556] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [560-575] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-578] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [586-601] for track '54' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [603-643] for track '54' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [518-519] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-527] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-551] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-620] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [622-656] for track '55' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [518-525] for track '56' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [518-519] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-540] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-545] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [553-569] for track '57' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [571-573] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [576-577] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-585] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-589] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [591-593] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [595-596] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-625] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [629-630] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-529] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [537-540] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [544-545] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-554] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [557-565] for track '58' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [621-623] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-533] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-539] for track '59' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [541-544] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-541] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-550] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-558] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-659] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [557-567] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [576-580] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [582-588] for track '62' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [590-596] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-623] for track '62' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [628-637] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-590] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [594-638] for track '64' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [584-589] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [592-593] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-607] for track '65' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [616-618] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [622-626] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-637] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [639-642] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [645-652] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-615] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [616-646] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-624] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-636] for track '69' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [640-646] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [648-651] for track '69' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [624-625] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [631-632] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [632-633] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [632-634] for track '72' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.