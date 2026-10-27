# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_373`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_373/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 748: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '20' (LG) duration 91 frames exceeds threshold 90 frames [start=111, end=201].
> - Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 91 frames exceeds threshold 90 frames [start=111, end=201].
> - Action 'Action_None' range [108-212] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-311] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [111-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [171-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-205] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [108-303] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-310] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-133] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-204] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-218] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-292] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [201-265] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-177] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [108-282] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-304] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-315] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-139] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-237] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-316] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-270] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-284] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [111-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-286] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [155-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-194] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-227] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-303] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-292] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-251] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-258] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-270] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-291] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-329] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-329] for track '33' has 2 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.