# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_19`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_19/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 163 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 659 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [134-339] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-347] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-367] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-374] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-623] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-659] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-323] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-381] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-393] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-458] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-627] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [633-641] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-330] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-433] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [443-472] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-66] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-282] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-479] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-484] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-563] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [576-582] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-293] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-315] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-457] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-659] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-292] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-315] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-339] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-598] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [605-607] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-277] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-429] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [432-437] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [440-659] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-255] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-341] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-418] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-221] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-229] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-251] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-307] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-339] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-623] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [626-631] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [634-640] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-64] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-207] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-328] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-334] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-615] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-433] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-659] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-264] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-275] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-423] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-205] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [207-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-264] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-291] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-331] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-341] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-394] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-399] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-414] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-422] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-633] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-286] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-333] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [335-341] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [134-190] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-306] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-333] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-659] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-331] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-413] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [416-426] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-435] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-479] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [483-484] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-494] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-626] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-445] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [450-659] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-580] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [432-659] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-489] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-627] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [631-641] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-541] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-551] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [553-574] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [593-598] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-615] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [618-620] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-549] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-607] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-659] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [608-609] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-615] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [630-635] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [648-651] for track '33' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.