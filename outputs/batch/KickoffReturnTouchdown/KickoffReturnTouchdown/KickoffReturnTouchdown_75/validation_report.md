# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_75`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 76 |
| Player Tracks | 76 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 210 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 151: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 152: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action 'Action_None' range [86-325] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-278] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-314] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-623] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-256] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-326] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-321] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-337] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-347] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [360-382] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [389-469] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-417] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-347] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [361-455] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-511] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-345] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-469] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-616] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-628] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-357] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-281] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-347] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [361-596] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-347] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-353] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [356-506] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-281] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-316] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-629] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-345] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-369] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [375-435] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [86-347] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [363-378] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [86-345] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-416] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [86-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-345] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-369] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-446] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-205] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-218] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-267] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [287-347] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [350-351] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [354-395] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-78] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-125] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-11] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-18] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-53] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-62] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-70] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-231] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-252] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-234] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-281] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-279] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-347] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-629] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-333] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-347] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-424] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-437] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-442] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-343] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-446] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [449-488] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-443] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-629] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-400] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-408] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [412-429] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-455] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-464] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-505] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-513] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-539] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [542-543] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-505] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-512] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-518] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-514] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-520] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-541] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [536-537] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-542] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [538-542] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-545] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [586-587] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [591-616] for track '54' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [554-555] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-611] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [615-620] for track '55' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [625-627] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-565] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-618] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-624] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [626-629] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-562] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-574] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-578] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-588] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [591-592] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-608] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [610-611] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [613-624] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-578] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-580] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [591-618] for track '61' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [578-588] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [590-628] for track '62' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [578-589] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [594-597] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-622] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [586-601] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [587-588] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [602-609] for track '65' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [592-598] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [594-596] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [605-611] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [614-615] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [603-618] for track '68' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [604-605] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [607-608] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-610] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [615-616] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [607-615] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [621-627] for track '71' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [611-614] for track '72' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [611-612] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [616-619] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-619] for track '75' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.