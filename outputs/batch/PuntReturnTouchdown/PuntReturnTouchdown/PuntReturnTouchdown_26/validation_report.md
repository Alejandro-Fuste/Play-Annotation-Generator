# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_26`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_26/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 52 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 185 |
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
> - Action 'Action_None' range [71-341] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-435] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-513] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-586] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-311] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-496] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [501-599] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-118] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-426] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [429-484] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-525] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [527-536] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [538-544] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-365] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-417] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-582] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-131] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-205] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-272] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-296] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-228] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-310] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-280] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-421] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-487] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-281] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-372] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-450] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [452-458] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-508] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-407] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-520] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-574] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [576-599] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-456] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-520] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-548] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-599] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-203] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-245] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-276] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-266] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-346] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-381] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-480] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-229] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-452] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-577] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-17] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-63] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '20' starts at frame 71, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [71-73] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-35] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '21' starts at frame 71, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [71-74] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-371] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-483] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [487-562] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [569-599] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-156] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-221] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-166] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-204] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-476] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [481-490] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-514] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [518-519] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-527] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-362] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-446] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-471] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-484] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-446] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [453-588] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-592] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [261-264] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [266-420] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [423-561] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [568-569] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [571-572] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '26' starts at frame 582, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [582-596] for track '26' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [187-442] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [446-447] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-468] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-442] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [448-502] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [509-536] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-572] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-599] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-415] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [417-530] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-591] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-366] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-418] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-457] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-342] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-358] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-376] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-406] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-488] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-384] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-391] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-489] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-452] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-510] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-515] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [527-533] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [538-545] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-576] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-503] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-599] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-501] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-544] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-551] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-568] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-576] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-599] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-589] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [593-598] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [586-589] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-596] for track '51' has 2 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.