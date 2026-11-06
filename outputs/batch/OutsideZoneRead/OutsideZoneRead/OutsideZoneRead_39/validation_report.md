# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_39`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 28 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 80: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '5' has invalid range: start=169, end=139. Clamping end to start.
> - Segment 'Action_PressEdge' for track '15' has invalid range: start=182, end=139. Clamping end to start.
> - Action 'Action_PreSnap' range [0-214] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-226] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-235] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-252] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-168] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [183-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [187-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-227] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-192] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-31] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-135] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-152] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-219] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-148] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-249] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-161] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-204] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-165] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-189] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-257] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-248] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-227] for track '28' has 2 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.