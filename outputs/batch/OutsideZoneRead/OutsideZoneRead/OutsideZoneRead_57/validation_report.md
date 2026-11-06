# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_57`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_57/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 81 |
| Player Tracks | 81 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 171 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 929 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 929 as fallback play end.
> - Action 'Action_PreSnap' range [0-427] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-296] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-427] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-427] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-316] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-427] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-342] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-368] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-379] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-280] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-358] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-370] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-427] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-427] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-275] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-297] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-293] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-331] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-339] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-350] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-427] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-429] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-320] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [143-189] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-427] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-282] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-303] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-427] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-427] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [143-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-414] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-427] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-427] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-264] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-267] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-284] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-277] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-427] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-322] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-429] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-334] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-427] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-427] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-427] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [424-429] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-429] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-779] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [809-814] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [841-868] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-817] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-782] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [785-800] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-528] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [533-538] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [546-790] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [795-855] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [858-915] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [923-928] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-840] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [842-929] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-789] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [791-839] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [869-876] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-500] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [508-819] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [826-874] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-505] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [512-643] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [650-786] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-797] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [799-920] for track '57' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-757] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [761-904] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-617] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [624-675] for track '59' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [689-732] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [734-929] for track '59' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-613] for track '60' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [617-644] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [665-929] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-789] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-558] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [602-613] for track '62' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [620-633] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [642-650] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-555] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-499] for track '64' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [502-755] for track '64' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [765-780] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [786-796] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [802-851] for track '64' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [760-763] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [780-804] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [778-788] for track '66' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [785-788] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [826-829] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [831-833] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [836-872] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [880-884] for track '67' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [887-904] for track '67' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [906-913] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [915-928] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [819-882] for track '68' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [887-888] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [828-895] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [833-839] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [837-839] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [840-929] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [852-855] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [862-923] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [863-871] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [879-915] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [923-924] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [891-910] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [913-915] for track '80' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.