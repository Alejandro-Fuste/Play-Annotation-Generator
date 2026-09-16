# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_101`
- **Input XML**: `output/BootPass/BootPass_101/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 196 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-349] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [220-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-309] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-318] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-378] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-387] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-240] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [249-262] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [266-318] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [321-358] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-374] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-380] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-369] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-385] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-238] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-389] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-237] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-251] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-320] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-351] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-247] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-318] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-364] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-373] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-355] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-255] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-255] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-287] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-337] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-240] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-255] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-278] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-314] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-276] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-295] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-314] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-389] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-323] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-336] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-350] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-332] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-341] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-353] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-338] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-348] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-370] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-362] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-376] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-389] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-366] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-374] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-387] for track '33' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.