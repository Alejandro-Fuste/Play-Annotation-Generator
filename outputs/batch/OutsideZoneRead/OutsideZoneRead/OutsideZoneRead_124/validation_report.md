# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_124`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_124/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 250: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [9–19], lower_priority='Action_ZoneBlock' annotated_start=12, effective_Action_ZoneBlock_start=20.
> - Action 'Action_None' range [9-28] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-54] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-95] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-71] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-71] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [51-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-39] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-16] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-60] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-18] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [9-11] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-50] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-85] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-154] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-154] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-184] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-187] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-202] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '32' has 3 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.