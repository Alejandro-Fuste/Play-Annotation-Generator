# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_97`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 96 frames exceeds threshold 90 frames [start=95, end=190].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [92–106], lower_priority='Action_ZoneBlock' annotated_start=95, effective_Action_ZoneBlock_start=107.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 96 frames exceeds threshold 90 frames [start=95, end=190].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 96 frames exceeds threshold 90 frames [start=95, end=190].
> - Action 'Action_None' range [92-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-202] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-185] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-166] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-182] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-227] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-237] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [132-161] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [164-172] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [184-188] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-148] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-223] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-226] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-207] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-237] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [128-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-190] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-149] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-197] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-239] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.