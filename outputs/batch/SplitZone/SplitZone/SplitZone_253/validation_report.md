# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_253`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_253/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 146 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 508: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 508: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 127 frames exceeds threshold 90 frames [start=106, end=232].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [103–114], lower_priority='Action_ZoneBlock' annotated_start=106, effective_Action_ZoneBlock_start=115.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 99 frames exceeds threshold 90 frames [start=106, end=204].
> - Action 'Action_None' range [103-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-126] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-315] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [108-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [137-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-226] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-291] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [311-323] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-134] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-328] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [143-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [272-301] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [307-336] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [338-343] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [350-352] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-271] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-289] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-166] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [150-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [179-216] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-209] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [150-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [203-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-193] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-296] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-199] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-311] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-350] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-194] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-195] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-215] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-309] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-317] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-213] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [219-277] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-323] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-332] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [337-354] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-297] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-231] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-284] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-359] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-235] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-274] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-301] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-329] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-316] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-289] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '37' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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