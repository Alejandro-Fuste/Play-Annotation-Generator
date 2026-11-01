# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_67`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 136: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 136: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 136: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 98 frames exceeds threshold 90 frames [start=83, end=180].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (C) duration 98 frames exceeds threshold 90 frames [start=83, end=180].
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [80–93], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=94.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 98 frames exceeds threshold 90 frames [start=83, end=180].
> - Action 'Action_None' range [80-321] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-256] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-312] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-230] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-270] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-329] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-186] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [193-260] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-286] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-297] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-307] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-313] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-307] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-197] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-132] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-181] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-290] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [126-310] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-216] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-207] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-307] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-324] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-322] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-329] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-202] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-229] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-213] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-329] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-329] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-322] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-327] for track '35' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.