# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_186`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_186/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 374: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (LG) duration 123 frames exceeds threshold 90 frames [start=212, end=334].
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 123 frames exceeds threshold 90 frames [start=212, end=334].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 123 frames exceeds threshold 90 frames [start=212, end=334].
> - Action 'Action_ZoneBlock' range [212-290] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [300-302] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [305-307] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [311-334] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [244-286] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-403] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-252] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-270] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-364] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-233] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-327] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-295] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-319] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-410] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-313] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [217-261] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-229] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-394] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-225] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-300] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-308] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-334] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-306] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-318] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-138] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-243] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-303] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-275] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-313] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-419] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-329] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-362] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-366] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-368] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-384] for track '37' has 2 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.