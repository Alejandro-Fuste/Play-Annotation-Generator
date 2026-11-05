# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_76`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 59 |
| Player Tracks | 59 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 182 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [11-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-406] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-518] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [525-561] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-224] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-88] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-108] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-437] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [439-523] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-535] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-568] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-194] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-114] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-342] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-461] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-466] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-227] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-263] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-338] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-44] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-528] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [530-599] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [11-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-279] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-301] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-347] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-39] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-387] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-36] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-308] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-71] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-177] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [179-382] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [386-451] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-323] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-350] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-328] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-467] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-471] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-30] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-266] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [286-295] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-325] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-362] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-376] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [388-392] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-405] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-272] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-292] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-379] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [216-291] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [380-392] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [394-410] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-107] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-137] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-182] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-320] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [327-372] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-129] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-282] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-311] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-325] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-346] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-371] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-389] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [394-418] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-354] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-194] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-313] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-190] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-289] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-400] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-403] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-407] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-318] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-416] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-334] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-356] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [360-364] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-318] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-371] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-391] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [394-435] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-361] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-378] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-383] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-388] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-411] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [413-420] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-413] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-436] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-491] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-514] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-475] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-483] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-513] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [481-569] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-572] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-574] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [558-575] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [568-571] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [575-593] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [576-599] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-582] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-588] for track '57' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.