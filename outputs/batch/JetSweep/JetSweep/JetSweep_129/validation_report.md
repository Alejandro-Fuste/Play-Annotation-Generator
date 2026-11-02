# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_129`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 135 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (RT) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
> - Validation warning: Action 'Action_LeadBlock' for track '18' (SAF1) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 110 frames exceeds threshold 90 frames [start=91, end=200].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [89–104], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=105.
> - Action 'Action_None' range [89-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-299] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-233] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-256] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-259] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-186] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-194] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-216] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-208] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-191] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [193-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-270] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-227] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-204] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-235] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-260] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [266-273] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-290] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-190] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-256] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [91-183] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [186-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-181] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-258] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-147] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-248] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-260] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-270] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-197] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-196] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-248] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-221] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-191] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-217] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-232] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-237] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-250] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-256] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-292] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-268] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-293] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '38' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.