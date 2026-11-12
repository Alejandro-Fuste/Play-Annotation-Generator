# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_27`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 56: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 99 frames exceeds threshold 90 frames [start=210, end=308].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 99 frames exceeds threshold 90 frames [start=210, end=308].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [207–223], lower_priority='Action_ZoneBlock' annotated_start=210, effective_Action_ZoneBlock_start=224.
> - Segment 'Action_BallCarry' for track '16' has invalid range: start=254, end=227. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 99 frames exceeds threshold 90 frames [start=210, end=308].
> - Action 'Action_None' range [207-418] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [214-308] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-385] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-390] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-400] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-310] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-360] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '11' starts at frame 224, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [224-224] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [237-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-443] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [445-500] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [503-504] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-513] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-527] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [535-536] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-539] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-528] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [530-533] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-342] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-531] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-538] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-227] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-536] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [210-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [284-289] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-275] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-285] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-305] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-228] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-283] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-323] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-314] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-325] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-346] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-463] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-492] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-521] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-528] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-390] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-396] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-414] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [418-426] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-431] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-450] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-470] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [472-490] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-510] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [513-515] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-525] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-539] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-410] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-420] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-444] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-520] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-488] for track '34' has 1 frames without a visible bounding box.
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