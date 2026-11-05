# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_44`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 59 |
| Player Tracks | 59 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 174 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [38-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-479] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-58] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-479] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-396] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-405] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-442] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-113] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-296] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [299-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-315] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-387] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-459] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-462] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-249] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-112] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-267] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-357] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-322] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-470] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-371] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-374] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-212] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-178] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-385] for track '23' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [390-439] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [224-368] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [370-374] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [376-418] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-142] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-160] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-279] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-381] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-274] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-310] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-320] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-375] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-400] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-205] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-403] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-405] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-471] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-406] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-335] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-366] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [381-387] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-450] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-324] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-423] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [427-429] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-439] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [442-452] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-359] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [361-365] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-371] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-383] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [405-450] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-394] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-404] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-429] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-380] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-394] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [403-423] for track '51' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [425-434] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [438-439] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-448] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-403] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-409] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-421] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [429-430] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-451] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-457] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-475] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-478] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-422] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-441] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [445-446] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-459] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-472] for track '56' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.