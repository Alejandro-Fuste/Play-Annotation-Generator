# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_126`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_126/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [142–157], lower_priority='Action_ZoneBlock' annotated_start=145, effective_Action_ZoneBlock_start=158.
> - Action 'Action_None' range [142-299] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-141] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [176-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [187-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [176-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [142-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-196] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-238] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-276] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-283] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-248] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-289] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.