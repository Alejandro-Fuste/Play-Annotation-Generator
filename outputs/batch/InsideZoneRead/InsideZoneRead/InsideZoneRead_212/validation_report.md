# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_212`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_212/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 424: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [210–224], lower_priority='Action_ZoneBlock' annotated_start=213, effective_Action_ZoneBlock_start=225.
> - Action 'Action_None' range [210-266] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-254] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-318] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-341] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-348] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-336] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-252] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [225-232] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [252-258] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [260-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [266-271] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-282] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-348] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-326] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-277] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-324] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-332] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-359] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-34] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-40] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [250-357] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-28] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-267] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-329] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-323] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.