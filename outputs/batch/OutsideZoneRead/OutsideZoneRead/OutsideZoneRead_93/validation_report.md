# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_93`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 188: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [17-88] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-97] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-103] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-111] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-156] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-128] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-242] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-78] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [66-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-200] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-199] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-188] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-246] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-250] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-240] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-255] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-252] for track '32' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.