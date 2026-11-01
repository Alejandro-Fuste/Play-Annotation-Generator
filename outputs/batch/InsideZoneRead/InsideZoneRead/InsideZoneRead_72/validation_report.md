# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_72`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_72/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 146: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 146: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 103 frames exceeds threshold 90 frames [start=79, end=181].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RG) duration 103 frames exceeds threshold 90 frames [start=79, end=181].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 103 frames exceeds threshold 90 frames [start=79, end=181].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [77–91], lower_priority='Action_ZoneBlock' annotated_start=79, effective_Action_ZoneBlock_start=92.
> - Segment 'Action_BallCarry' for track '12' has invalid range: start=117, end=81. Clamping end to start.
> - Action 'Action_ZoneBlock' range [79-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-173] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-229] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-206] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-152] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-185] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-207] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-227] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-196] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [118-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [131-181] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-18] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-24] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-73] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-199] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-113] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-154] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-204] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-239] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '27' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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