# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_105`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_105/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 99 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 212: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 212: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=19.
> - Action 'Action_None' range [3-193] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-82] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-29] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-239] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-44] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-237] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [3-38] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-117] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 65, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [65-74] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-99] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-97] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [41-235] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [3-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-164] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-24] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-10] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-103] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-134] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-213] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-220] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-200] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.