# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_92`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 92 frames exceeds threshold 90 frames [start=138, end=229].
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 92 frames exceeds threshold 90 frames [start=138, end=229].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [135–150], lower_priority='Action_ZoneBlock' annotated_start=138, effective_Action_ZoneBlock_start=151.
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (RG) duration 92 frames exceeds threshold 90 frames [start=138, end=229].
> - Action 'Action_PreSnap' range [0-181] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [190-242] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [244-276] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-229] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-277] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-326] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-232] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-322] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-207] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-285] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [162-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [197-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [205-229] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-283] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-301] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-258] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-268] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-297] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-290] for track '19' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.