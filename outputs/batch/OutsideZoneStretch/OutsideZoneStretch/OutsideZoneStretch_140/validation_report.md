# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_140`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_140/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PreSnap' range [0-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-342] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-367] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-401] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-357] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-242] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-404] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-352] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-449] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-152] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-211] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-224] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-250] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-303] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [238-301] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-387] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-449] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 178, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [178-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-390] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-420] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-129] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-314] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-340] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-367] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-350] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-191] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-410] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-249] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-258] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-413] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-235] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-255] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-349] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-226] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-336] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-230] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-238] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-247] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-267] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-410] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-284] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-300] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-305] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-367] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-324] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-330] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-360] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-392] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-401] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-406] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-322] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-333] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-343] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-352] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-357] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-390] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-404] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-436] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-444] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [441-443] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [441-449] for track '39' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.