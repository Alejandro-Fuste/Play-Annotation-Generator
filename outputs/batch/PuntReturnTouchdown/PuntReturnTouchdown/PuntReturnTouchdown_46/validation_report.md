# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_46`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 94: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 94: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [77-314] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-396] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-344] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-346] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [349-379] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-470] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-383] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-408] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-413] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-424] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-281] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-80] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-479] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-373] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-456] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-479] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-377] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-304] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-310] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-447] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-267] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-294] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-318] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-383] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-240] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-268] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-287] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-216] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-470] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-379] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-396] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [401-479] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-95] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-107] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [185-318] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [321-328] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [331-344] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [347-371] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [373-374] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-460] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-308] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-319] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-333] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-338] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-254] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-311] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-358] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-361] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-377] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-371] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-479] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-467] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-465] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [430-438] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-455] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-460] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-449] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-437] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-473] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-448] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-453] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-462] for track '48' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.