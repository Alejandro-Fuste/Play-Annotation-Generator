# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_203`
- **Input XML**: `outputs/batch/Power/Power/Power_203/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 65 |
| Player Tracks | 65 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 141 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Action 'Action_PreSnap' range [18-509] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-308] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-392] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [232-264] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [267-303] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-340] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-364] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-420] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-345] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-483] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [485-487] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [489-509] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-386] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-393] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-285] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-285] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-298] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-359] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-373] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-255] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-265] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-344] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-381] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-509] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-244] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-253] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-256] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-319] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-509] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-454] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-284] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-316] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-332] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-338] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-343] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-301] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-34] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-380] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [232-283] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-245] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-357] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-255] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-308] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-347] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-405] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-298] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-301] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-331] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-275] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-295] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-289] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-312] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-400] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-485] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-352] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-307] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-375] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-377] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-412] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-422] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [425-429] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [433-434] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [478-479] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-380] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-386] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-388] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-395] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-397] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-398] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-406] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-405] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [417-418] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-402] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-408] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [411-412] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-417] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-417] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [421-422] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [485-486] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [423-425] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [424-425] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [430-432] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-432] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [431-432] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-436] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [433-435] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [433-435] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [445-446] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [448-450] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [452-454] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [461-462] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [466-471] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [482-485] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [488-489] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [492-493] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [501-503] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [464-467] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [466-467] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [471-472] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-493] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [502-509] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [477-478] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [480-509] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [482-483] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [489-495] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [504-509] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [501-505] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [507-508] for track '64' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.