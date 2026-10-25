# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_101`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_101/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 182: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [188–196], lower_priority='Action_RunBlock' annotated_start=196, effective_Action_RunBlock_start=197.
> - Action 'Action_None' range [188-349] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [220-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [196-240] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [248-309] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [317-318] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-378] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-240] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [249-262] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [266-318] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [321-358] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-374] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-380] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-369] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-385] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-244] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [196-217] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-232] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-389] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-227] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [197-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [248-251] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [254-255] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [257-258] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [307-320] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [324-351] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-240] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-318] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-364] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-373] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [196-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [264-355] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-255] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [196-244] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [248-255] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [285-287] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [289-337] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [339-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-240] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-278] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-314] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-314] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-389] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-323] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-336] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-332] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-341] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-338] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-370] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-362] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-376] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-389] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-366] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-374] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-387] for track '33' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.