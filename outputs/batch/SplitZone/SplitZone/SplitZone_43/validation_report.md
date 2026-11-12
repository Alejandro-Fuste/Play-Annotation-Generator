# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_43`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [74–89], lower_priority='Action_ZoneBlock' annotated_start=77, effective_Action_ZoneBlock_start=90.
> - Segment 'Action_ZoneBlock' for track '21' has invalid range: start=77, end=23. Clamping end to start.
> - Action 'Action_None' range [74-167] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-291] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-298] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-259] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-284] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-326] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-295] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-314] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-326] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-199] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-105] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-302] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-316] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-138] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-322] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [74-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-261] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-302] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [307-308] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-231] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-10] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-189] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-231] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-303] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-224] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-311] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-329] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-253] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-297] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-329] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '39' has 1 frames without a visible bounding box.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.