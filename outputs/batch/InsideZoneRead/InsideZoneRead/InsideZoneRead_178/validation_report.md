# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_178`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_178/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 356: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - Row 356: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [180–193], lower_priority='Action_ZoneBlock' annotated_start=183, effective_Action_ZoneBlock_start=194.
> - Action 'Action_None' range [180-389] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-297] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-331] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-389] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-317] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-389] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-211] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-381] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-387] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-312] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-203] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [210-251] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [253-256] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-278] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-288] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-313] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-262] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-348] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-389] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-294] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-303] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-343] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-211] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-361] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [376-377] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-270] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-298] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-311] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [321-389] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-389] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.