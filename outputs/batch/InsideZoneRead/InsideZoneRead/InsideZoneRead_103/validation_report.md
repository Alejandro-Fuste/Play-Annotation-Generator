# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_103`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_103/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [40–54], lower_priority='Action_ZoneBlock' annotated_start=42, effective_Action_ZoneBlock_start=55.
> - Action 'Action_None' range [40-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-199] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-207] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-109] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [40-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-78] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [86-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [111-117] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-184] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [65-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-171] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-193] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-116] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-169] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.