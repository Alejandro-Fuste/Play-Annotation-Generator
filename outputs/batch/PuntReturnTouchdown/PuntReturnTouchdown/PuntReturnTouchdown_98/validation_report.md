# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_98`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_98/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 66 |
| Player Tracks | 66 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 221 |
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
> - Action 'Action_None' range [17-474] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-477] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-593] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-629] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-60] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-416] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-425] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-430] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-62] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-381] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-500] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-163] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-231] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-260] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-272] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-286] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-292] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-300] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-311] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-338] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-384] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-491] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-94] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-451] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-370] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-459] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [462-602] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-607] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [613-619] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-235] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-391] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [393-416] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-474] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-488] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-484] for track '10' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [17-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-249] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-373] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-104] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [232-265] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [272-305] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-370] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-400] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-294] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [300-355] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-27] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-103] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-258] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-319] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-366] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-423] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [432-435] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-332] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-351] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-423] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-629] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-332] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-419] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-464] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-506] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-547] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-317] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [319-328] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-355] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-395] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-443] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-449] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-456] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-471] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-491] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-386] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-419] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-430] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-433] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-440] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-481] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-414] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-317] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-390] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-403] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-421] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [436-442] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [483-484] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-493] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [530-533] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-586] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [589-592] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-507] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-495] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-331] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-343] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-354] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-373] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-484] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-493] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-364] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-376] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-381] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-393] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-415] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-416] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-393] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-464] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-493] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [505-507] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-412] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-493] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [519-606] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [610-629] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-483] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-448] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-456] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-507] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [509-519] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-455] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-488] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-493] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-461] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-469] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-476] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-566] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-593] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-605] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-493] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-497] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [516-518] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-527] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-593] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-521] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-530] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-537] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-545] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [522-529] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-547] for track '57' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [562-575] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-593] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-600] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-605] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-544] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [552-606] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [610-626] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-566] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-570] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [578-580] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [582-586] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-590] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-592] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [597-605] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [598-627] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [600-612] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [615-617] for track '65' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.