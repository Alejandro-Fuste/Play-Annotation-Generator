# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_163`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_163/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 328: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 328: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 127 frames exceeds threshold 90 frames [start=118, end=244].
> - Validation warning: Action 'Action_LeadBlock' for track '5' (TE) duration 127 frames exceeds threshold 90 frames [start=118, end=244].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (RG) duration 110 frames exceeds threshold 90 frames [start=118, end=227].
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [117–130], lower_priority='Action_ZoneBlock' annotated_start=118, effective_Action_ZoneBlock_start=131.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 93 frames exceeds threshold 90 frames [start=118, end=210].
> - Action 'Action_None' range [117-202] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [140-238] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [240-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-345] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-203] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-213] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-224] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [118-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [205-212] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [214-217] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-313] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-203] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-231] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-319] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-271] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-279] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-342] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-349] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-278] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-315] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-190] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [117-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-210] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-223] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-229] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-334] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-265] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-322] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-327] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-346] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-337] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-346] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-356] for track '34' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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