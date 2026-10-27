# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_91`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 337 targets track ID '378', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 184: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 184: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 184: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PreSnap' range [0-292] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [293-343] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-122] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-285] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-308] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [293-312] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-110] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [320-378] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [381-409] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-343] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [296-390] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-322] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-325] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-292] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [296-368] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-335] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-400] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-408] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-235] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-292] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-350] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-323] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-295] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [296-369] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-292] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-313] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-312] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-362] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-332] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-353] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-292] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-337] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-279] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-238] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-359] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-350] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-360] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-375] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-345] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-348] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-345] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-449] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [403-404] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-418] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [420-421] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-435] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-442] for track '41' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.