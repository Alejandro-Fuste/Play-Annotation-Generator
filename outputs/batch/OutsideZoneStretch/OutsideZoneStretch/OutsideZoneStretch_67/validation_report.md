# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_67`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 136: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [0-374] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-320] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-386] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-308] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-220] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [230-256] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-292] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-233] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-243] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-356] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-388] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-301] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [213-245] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 258, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [258-258] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-283] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [285-292] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-389] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-379] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-214] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-296] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-325] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-379] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-278] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-389] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-220] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [223-232] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-264] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-386] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-356] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-265] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-278] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-287] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-296] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-300] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-303] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-313] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-310] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-383] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-388] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-308] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-325] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-331] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-369] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [371-372] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-377] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-385] for track '33' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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