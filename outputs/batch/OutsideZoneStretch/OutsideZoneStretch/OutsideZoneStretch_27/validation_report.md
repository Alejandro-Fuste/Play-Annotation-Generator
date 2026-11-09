# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_27`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 56: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-226] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-270] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-274] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-215] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-287] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-335] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-348] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-357] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-233] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-228] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [182-228] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-301] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-319] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-328] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-100] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-139] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-228] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-89] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-266] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-281] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [178-184] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-290] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-330] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-214] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-275] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-291] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-240] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-268] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-231] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-348] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-277] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-295] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-281] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-352] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-288] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-319] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-324] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-357] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-344] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-351] for track '36' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.