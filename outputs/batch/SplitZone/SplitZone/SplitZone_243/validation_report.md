# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_243`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_243/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (LG) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [64–78], lower_priority='Action_ZoneBlock' annotated_start=67, effective_Action_ZoneBlock_start=79.
> - Action 'Action_None' range [64-151] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-244] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-249] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-167] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-269] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-208] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-212] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [98-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [151-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [157-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-186] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-245] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [247-256] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-212] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-224] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-211] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [152-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-235] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [97-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-212] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-259] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-220] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-230] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-256] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-123] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-221] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-167] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-196] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-219] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-222] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-231] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-256] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-212] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-222] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-249] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-269] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-265] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-252] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-259] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.