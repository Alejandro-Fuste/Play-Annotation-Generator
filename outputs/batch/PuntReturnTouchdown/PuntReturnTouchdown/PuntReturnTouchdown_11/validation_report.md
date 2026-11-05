# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_11`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 50 |
| Player Tracks | 50 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 188 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [30-164] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-345] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-360] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [362-365] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-83] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [85-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-213] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-569] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [30-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-244] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-259] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-530] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-180] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [30-186] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-451] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [463-569] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-547] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [30-242] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-510] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [30-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-569] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-177] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-223] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-217] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-399] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-162] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-193] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-273] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-569] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-569] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-549] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [553-569] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-371] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-350] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-360] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-366] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-382] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-226] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-569] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-115] for track '21' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-156] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-171] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [197-213] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [215-511] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [524-525] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [530-535] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [539-564] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-216] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-209] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-234] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-279] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-287] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-331] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-569] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-335] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [337-345] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-535] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [538-540] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-549] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [551-569] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-358] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [363-516] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-524] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-556] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [559-561] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-374] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-408] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-427] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-466] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-478] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-492] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-498] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [500-504] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-537] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-542] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-551] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-305] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-388] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-569] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-356] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-557] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-569] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [394-396] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-401] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-463] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-469] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-489] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [494-497] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-507] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-548] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [485-490] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-502] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-523] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [531-540] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-551] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-564] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-569] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-507] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [514-527] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [533-534] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-538] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-541] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-544] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-505] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-512] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [517-519] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-526] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-514] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [531-532] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [532-542] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-545] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-569] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-557] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-565] for track '49' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.