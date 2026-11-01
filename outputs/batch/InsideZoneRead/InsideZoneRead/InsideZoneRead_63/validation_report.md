# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_63`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
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
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [44–54], lower_priority='Action_ZoneBlock' annotated_start=47, effective_Action_ZoneBlock_start=55.
> - Action 'Action_None' range [44-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-157] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-102] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-163] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-174] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-184] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-146] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-131] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-181] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-221] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-211] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-239] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-71] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-89] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-109] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [176-177] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-137] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-202] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '26' has 1 frames without a visible bounding box.
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