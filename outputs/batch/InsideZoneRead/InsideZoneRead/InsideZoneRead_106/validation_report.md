# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_106`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 214: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 214: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [52–65], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=66.
> - Action 'Action_None' range [52-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-212] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-79] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-170] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-287] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [85-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-236] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 119, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [119-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-213] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [52-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-98] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-118] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-234] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-131] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-289] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-272] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-267] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-257] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-274] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [290-293] for track '35' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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