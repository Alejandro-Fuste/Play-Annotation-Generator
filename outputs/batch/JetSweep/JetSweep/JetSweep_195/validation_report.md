# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_195`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_195/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '0' (WR1) duration 148 frames exceeds threshold 90 frames [start=83, end=230].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 148 frames exceeds threshold 90 frames [start=83, end=230].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 148 frames exceeds threshold 90 frames [start=83, end=230].
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [82–96], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=97.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 148 frames exceeds threshold 90 frames [start=83, end=230].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 95 frames exceeds threshold 90 frames [start=83, end=177].
> - Action 'Action_LeadBlock' range [83-230] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [107-224] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [228-229] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-258] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-266] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-256] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-254] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-258] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-260] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-256] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-152] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-254] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-104] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-230] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-261] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-177] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-207] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-252] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-220] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-263] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-235] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '32' has 1 frames without a visible bounding box.
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