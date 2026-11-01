# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_91`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 124 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 98 frames exceeds threshold 90 frames [start=142, end=239].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [140–156], lower_priority='Action_ZoneBlock' annotated_start=142, effective_Action_ZoneBlock_start=157.
> - Segment 'Action_BallCarry' for track '21' has invalid range: start=181, end=163. Clamping end to start.
> - Action 'Action_None' range [140-197] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-303] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-281] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-329] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [140-176] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-211] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [163-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [197-199] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [201-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [211-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-329] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-196] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-141] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-217] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [140-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [190-196] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [201-206] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [226-229] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-261] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [263-289] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-296] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-153] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [203-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-221] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-279] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-294] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-300] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-242] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-287] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-322] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-289] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-284] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-300] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-312] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-310] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-329] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-329] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-314] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-324] for track '35' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.