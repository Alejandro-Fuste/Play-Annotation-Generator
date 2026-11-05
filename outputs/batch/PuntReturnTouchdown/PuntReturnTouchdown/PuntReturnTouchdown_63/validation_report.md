# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_63`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 54 |
| Player Tracks | 54 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 134 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 128: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [36-254] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-262] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-311] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-316] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-561] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-569] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-185] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-599] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-486] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-497] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [499-512] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-328] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-422] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-486] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-318] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-545] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-442] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-264] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-599] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-380] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-199] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-429] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-251] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-354] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-361] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-370] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-540] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [258-358] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [362-380] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [390-411] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-486] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-599] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-248] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-254] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-343] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-431] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-438] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-480] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-546] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-338] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-367] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-405] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-296] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-324] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-303] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-437] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-361] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-370] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-401] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-531] for track '40' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [536-537] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-599] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-486] for track '41' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [488-508] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-586] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-377] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-385] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-430] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-401] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-422] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-482] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-497] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-514] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-521] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-526] for track '52' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.