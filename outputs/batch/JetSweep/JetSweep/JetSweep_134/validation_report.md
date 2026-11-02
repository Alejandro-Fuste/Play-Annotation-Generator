# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_134`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_134/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '2' (LT) duration 91 frames exceeds threshold 90 frames [start=80, end=170].
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 124 frames exceeds threshold 90 frames [start=47, end=170].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 99 frames exceeds threshold 90 frames [start=47, end=145].
> - Validation warning: Action 'Action_LeadBlock' for track '6' (RB) duration 124 frames exceeds threshold 90 frames [start=47, end=170].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (LG) duration 124 frames exceeds threshold 90 frames [start=47, end=170].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 124 frames exceeds threshold 90 frames [start=47, end=170].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [46–64], lower_priority='Action_ZoneBlock' annotated_start=47, effective_Action_ZoneBlock_start=65.
> - Action 'Action_None' range [46-251] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [47-154] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [161-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-290] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-117] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-279] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-257] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-244] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-147] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [30-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-276] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-300] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-359] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-237] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-311] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-341] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-321] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-290] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-252] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-282] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '31' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.