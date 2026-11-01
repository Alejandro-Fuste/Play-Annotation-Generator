# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_41`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 83: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 84: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Row 84: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [188-236] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-270] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-219] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-291] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-221] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-226] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-254] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-284] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-316] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-324] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.