# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_199`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_199/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 118 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 349 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 349 as fallback play end.
> - Action 'Action_PreSnap' range [0-52] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-67] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-270] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-349] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-29] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-290] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-64] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-70] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-252] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-349] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-328] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-344] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-25] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-237] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-342] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [257-278] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [280-281] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [288-294] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 295, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [295-295] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-54] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-63] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-256] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [257-263] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [264-290] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [292-293] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-271] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-278] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-243] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-262] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-298] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-349] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-323] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-349] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [257-275] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-96] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-220] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-265] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-291] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-315] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-319] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-340] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-348] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-230] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-245] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-287] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-305] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-204] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [257-283] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-300] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-214] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-349] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-250] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-285] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-310] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-329] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-343] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-320] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-327] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-331] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-346] for track '32' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.