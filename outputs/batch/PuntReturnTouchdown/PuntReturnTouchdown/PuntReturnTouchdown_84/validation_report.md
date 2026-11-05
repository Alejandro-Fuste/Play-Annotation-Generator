# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_84`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_84/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 71 |
| Player Tracks | 71 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 241 |
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
> - Action 'Action_None' range [25-146] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-212] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-241] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-414] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-102] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-209] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [84-320] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-347] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-398] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-453] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-470] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-477] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-488] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-496] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [498-500] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [502-506] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-520] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [524-550] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [561-573] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [577-659] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [25-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-126] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-251] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-449] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-453] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-360] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-480] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [485-531] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-538] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-543] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-549] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-138] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-442] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [444-458] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-467] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-659] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-44] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-317] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-338] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-384] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-472] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-600] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [607-609] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-659] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-289] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-374] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-380] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-383] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-447] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-230] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-336] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-455] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [486-487] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-468] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [470-486] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [532-613] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-305] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-467] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-467] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-129] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-202] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-162] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-199] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-169] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-280] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-256] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-352] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [357-392] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-402] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-452] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-321] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-448] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [454-458] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-513] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [516-524] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [527-568] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [570-636] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [640-643] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-296] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-412] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-557] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [564-579] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [581-659] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-488] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [490-596] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-331] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-373] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-391] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-462] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-486] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-531] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-309] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-404] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-572] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [574-578] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-582] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-591] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [593-599] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [601-609] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-659] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-368] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-362] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-366] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-378] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-381] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-369] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-455] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-488] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-522] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-378] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-397] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-436] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-441] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-449] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-529] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [544-545] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-549] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-462] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [468-474] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-544] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [546-551] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [556-659] for track '47' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [407-444] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [463-465] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-474] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-510] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-411] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-442] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-659] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-431] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-435] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-438] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-442] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-448] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-446] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-451] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-479] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-462] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [463-636] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-470] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-476] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [471-474] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-516] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-529] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-538] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-545] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-576] for track '59' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [484-486] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-553] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [557-567] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [574-593] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [530-531] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-579] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-591] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-596] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-589] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [595-596] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [609-612] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [619-642] for track '66' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [612-613] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [615-652] for track '67' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [613-620] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [650-659] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [657-658] for track '70' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.