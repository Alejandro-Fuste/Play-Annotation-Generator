# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_69`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 125 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [77–90], lower_priority='Action_ZoneBlock' annotated_start=80, effective_Action_ZoneBlock_start=91.
> - Action 'Action_None' range [125-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-133] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-184] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-171] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-195] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-195] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [197-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-194] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-238] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [115-254] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-157] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-259] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-195] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-203] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-238] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-186] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-238] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-202] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [208-227] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-204] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [208-269] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-261] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-227] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-266] for track '32' has 3 frames without a visible bounding box.
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