# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_299`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_299/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 598: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [17–29], lower_priority='Action_ZoneBlock' annotated_start=20, effective_Action_ZoneBlock_start=30.
> - Action 'Action_None' range [17-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-177] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-80] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-68] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-210] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [17-26] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-93] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [34-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [62-174] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [176-178] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [187-200] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-202] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '27' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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