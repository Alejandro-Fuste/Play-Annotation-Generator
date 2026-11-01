# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_98`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_98/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [166–178], lower_priority='Action_ZoneBlock' annotated_start=167, effective_Action_ZoneBlock_start=179.
> - Action 'Action_None' range [165-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-233] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-266] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-226] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-271] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-249] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [182-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [196-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-270] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-223] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-260] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-290] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-202] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [215-237] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [243-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [251-254] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-174] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [176-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [182-243] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [245-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [187-191] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [166-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-272] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-286] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-259] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-281] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-220] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-253] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-278] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-280] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-274] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-297] for track '25' has 2 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.