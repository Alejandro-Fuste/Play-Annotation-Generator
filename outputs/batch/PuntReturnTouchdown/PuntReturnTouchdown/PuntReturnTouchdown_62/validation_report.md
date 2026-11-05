# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_62`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 82 |
| Player Tracks | 82 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 184 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 719 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [41-657] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-348] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-507] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-719] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-719] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-330] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-365] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-372] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-380] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-389] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-486] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-584] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-719] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-339] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-454] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-650] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-719] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-302] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-419] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-148] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-255] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-281] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-133] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-231] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-224] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-236] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-545] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-346] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-506] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-359] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [365-478] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-524] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-535] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [537-583] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [587-719] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-351] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-332] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-332] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-261] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-272] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-298] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-326] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-332] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-337] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-279] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-288] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-300] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-510] for track '33' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [513-623] for track '33' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [625-655] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-538] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-324] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-330] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-345] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-354] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [357-359] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-368] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-380] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-400] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-409] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-375] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-383] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-390] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-398] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-339] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-507] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-424] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-512] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-536] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-542] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-547] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-521] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-527] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-431] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-543] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-507] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-560] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-488] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-555] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [528-604] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [607-615] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-719] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-558] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [564-577] for track '54' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [568-583] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-597] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-588] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [570-594] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-597] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-593] for track '58' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [575-576] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-585] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [582-583] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [591-593] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [607-608] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [619-621] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [626-629] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [634-635] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [638-639] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [639-644] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [641-642] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [658-668] for track '69' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [705-712] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [659-660] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [666-668] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [686-687] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [689-690] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [708-711] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [674-706] for track '72' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [685-691] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [693-696] for track '73' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [699-702] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [707-716] for track '73' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [692-697] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [699-713] for track '75' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [693-694] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [699-714] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [707-712] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [708-713] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [712-719] for track '81' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.