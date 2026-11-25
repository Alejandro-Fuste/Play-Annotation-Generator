# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_190`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_190/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 379: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 379: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 379: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 380: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [17-210] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-170] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-72] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-170] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [64-73] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [78-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [187-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-170] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-125] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-174] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [45-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 100, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [100-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-84] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-149] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-170] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-88] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-170] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-156] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '26' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_190'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.