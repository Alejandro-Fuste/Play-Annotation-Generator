# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_104`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_104/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 210: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 109 frames exceeds threshold 90 frames [start=92, end=200].
> - Validation warning: Action 'Action_BlockSecondLevel' for track '6' (OLB1) duration 92 frames exceeds threshold 90 frames [start=109, end=200].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 109 frames exceeds threshold 90 frames [start=92, end=200].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 109 frames exceeds threshold 90 frames [start=92, end=200].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [89–103], lower_priority='Action_ZoneBlock' annotated_start=92, effective_Action_ZoneBlock_start=104.
> - Action 'Action_None' range [89-136] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-184] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-212] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [143-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-200] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-286] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [96-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [137-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [148-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-223] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-168] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [176-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [186-188] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-276] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-137] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-124] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-192] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-266] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-297] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-12] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-55] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-12] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-143] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [132-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-198] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-191] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-216] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-260] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-249] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-264] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-194] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-215] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-243] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-223] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-221] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-257] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-265] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-254] for track '30' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.