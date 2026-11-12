# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_187`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_187/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 376: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 150 frames exceeds threshold 90 frames [start=95, end=244].
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 150 frames exceeds threshold 90 frames [start=95, end=244].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 150 frames exceeds threshold 90 frames [start=95, end=244].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [92–103], lower_priority='Action_ZoneBlock' annotated_start=95, effective_Action_ZoneBlock_start=104.
> - Action 'Action_None' range [92-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-170] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [179-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-161] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [188-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-197] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-252] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [122-127] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-194] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [92-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [97-152] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-198] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-242] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-299] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-157] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-260] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [150-169] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [173-177] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [179-244] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-270] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-164] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-188] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-282] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-16] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-98] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-245] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-288] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-299] for track '28' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [224-233] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.