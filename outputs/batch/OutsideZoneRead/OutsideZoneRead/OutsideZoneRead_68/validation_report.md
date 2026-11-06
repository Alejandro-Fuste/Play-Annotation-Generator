# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_68`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_68/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 138: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [0-237] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-319] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-346] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-398] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-263] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-274] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-342] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-387] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-400] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [410-419] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-277] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-385] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-295] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-382] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-223] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [191-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-291] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-246] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-292] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-369] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-378] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-386] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-227] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-275] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [186-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [250-252] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-403] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-261] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-366] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-252] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-401] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-407] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [410-411] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-257] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-269] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-246] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-314] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-410] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-263] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-271] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-410] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-248] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-419] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-261] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-398] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-386] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-395] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-398] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-413] for track '26' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.