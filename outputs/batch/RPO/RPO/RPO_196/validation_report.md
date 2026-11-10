# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_196`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_196/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['LG', 'LT', 'RG'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-72] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-166] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-311] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-306] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-319] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-152] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-249] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-250] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [55-89] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [93-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [102-271] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [93-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [97-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-208] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-262] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-22] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-245] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-122] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-76] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-288] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-223] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-287] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-289] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-237] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-271] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-329] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-252] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-287] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-295] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-273] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-329] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-276] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-293] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-305] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-313] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-312] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-329] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-329] for track '33' has 1 frames without a visible bounding box.
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