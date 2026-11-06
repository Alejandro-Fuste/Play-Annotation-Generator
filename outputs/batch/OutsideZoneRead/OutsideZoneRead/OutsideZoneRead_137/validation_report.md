# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_137`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_137/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [12–28], lower_priority='Action_ZoneBlock' annotated_start=15, effective_Action_ZoneBlock_start=29.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 97 frames exceeds threshold 90 frames [start=15, end=111].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (LG) duration 97 frames exceeds threshold 90 frames [start=15, end=111].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 97 frames exceeds threshold 90 frames [start=15, end=111].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 97 frames exceeds threshold 90 frames [start=15, end=111].
> - Action 'Action_None' range [12-194] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-213] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-224] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-193] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [198-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-229] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-133] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-86] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-225] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [12-24] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [63-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-185] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-224] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [12-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-160] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-213] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [15-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-186] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-228] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [15-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-185] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-173] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-185] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-184] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-236] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [15-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-55] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-107] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-239] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-107] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-152] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-177] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-183] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-212] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-223] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '26' has 1 frames without a visible bounding box.
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