# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_234`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_234/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 104 frames exceeds threshold 90 frames [start=172, end=275].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 104 frames exceeds threshold 90 frames [start=172, end=275].
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [169–181], lower_priority='Action_ZoneBlock' annotated_start=172, effective_Action_ZoneBlock_start=182.
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 98 frames exceeds threshold 90 frames [start=172, end=269].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (RG) duration 101 frames exceeds threshold 90 frames [start=172, end=272].
> - Action 'Action_None' range [169-267] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-240] for track '4' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-260] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [182-234] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [238-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-313] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [179-221] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-353] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-245] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [197-204] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [206-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [209-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-267] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-272] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-248] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-324] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-265] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-270] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-254] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-284] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-258] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [262-323] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-298] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-273] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-288] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-270] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-318] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-343] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.