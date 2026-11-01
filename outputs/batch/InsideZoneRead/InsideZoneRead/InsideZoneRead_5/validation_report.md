# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_5`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 11: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 104 frames exceeds threshold 90 frames [start=83, end=186].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 104 frames exceeds threshold 90 frames [start=83, end=186].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 104 frames exceeds threshold 90 frames [start=83, end=186].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [81–98], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=99.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 104 frames exceeds threshold 90 frames [start=83, end=186].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 104 frames exceeds threshold 90 frames [start=83, end=186].
> - Action 'Action_None' range [81-157] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-191] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-205] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [118-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-236] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-257] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-119] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-139] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-259] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-228] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-248] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-283] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-216] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [131-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-143] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-152] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-240] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-262] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-137] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-281] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-238] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.