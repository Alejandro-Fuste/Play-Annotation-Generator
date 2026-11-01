# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_50`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 102: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 101 frames exceeds threshold 90 frames [start=136, end=236].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 101 frames exceeds threshold 90 frames [start=136, end=236].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 101 frames exceeds threshold 90 frames [start=136, end=236].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [134–152], lower_priority='Action_ZoneBlock' annotated_start=136, effective_Action_ZoneBlock_start=153.
> - Action 'Action_PreSnap' range [0-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [175-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-224] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [237-250] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-203] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-215] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [155-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-209] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-283] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-220] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-324] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-315] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [178-198] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-290] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-189] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-324] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-244] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-294] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-236] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [237-256] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-301] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-223] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-304] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-304] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-252] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-280] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-281] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-329] for track '25' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.