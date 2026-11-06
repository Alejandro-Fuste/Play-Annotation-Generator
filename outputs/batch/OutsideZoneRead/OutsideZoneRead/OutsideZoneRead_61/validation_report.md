# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_61`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 124: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 124: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-271] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-264] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [267-286] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-299] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-304] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-203] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-233] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-238] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [173-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-325] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-160] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-191] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-177] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-318] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-290] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-309] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-259] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-325] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-197] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-220] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-232] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-274] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-278] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-284] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-305] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-255] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-297] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-313] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-318] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-320] for track '31' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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