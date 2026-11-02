# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_185`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_185/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 99 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '1' (TE) duration 127 frames exceeds threshold 90 frames [start=77, end=203].
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 128 frames exceeds threshold 90 frames [start=77, end=204].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [74–92], lower_priority='Action_ZoneBlock' annotated_start=77, effective_Action_ZoneBlock_start=93.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 128 frames exceeds threshold 90 frames [start=77, end=204].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 128 frames exceeds threshold 90 frames [start=77, end=204].
> - Action 'Action_None' range [74-288] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-302] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [77-203] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-293] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [74-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-225] for track '4' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [229-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-276] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-273] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-153] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-205] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-284] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-304] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-315] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-254] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-213] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-237] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-251] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-220] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-241] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-217] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-149] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-243] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-85] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-100] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-66] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-209] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-291] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-204] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-237] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-257] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-204] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-243] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-295] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-324] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.