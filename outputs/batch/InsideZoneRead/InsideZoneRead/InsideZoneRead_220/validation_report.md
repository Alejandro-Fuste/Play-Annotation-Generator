# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_220`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_220/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 122 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 440: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 440: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [109–125], lower_priority='Action_ZoneBlock' annotated_start=112, effective_Action_ZoneBlock_start=126.
> - Action 'Action_None' range [109-275] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-131] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-219] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-234] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-272] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-189] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-278] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-322] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-196] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-225] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-166] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-184] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-252] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-261] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-305] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-263] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-272] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-291] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-197] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-124] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [109-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [124-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-129] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-252] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-189] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-209] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-229] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-242] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-252] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-263] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-260] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-300] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-293] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-323] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-320] for track '37' has 2 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.