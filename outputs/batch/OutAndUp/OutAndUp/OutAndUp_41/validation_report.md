# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_41`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 137 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [12–19], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=20.
> - Action 'Action_None' range [12-150] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-144] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-134] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-193] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [89-234] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [237-238] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [255-269] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-80] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-251] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-28] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-77] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [86-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-105] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-131] for track '9' has 6 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [134-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [145-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [154-164] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [182-189] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-194] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-269] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-138] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [144-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [164-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-230] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-154] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-166] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-160] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-216] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-269] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-103] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [12-125] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-143] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-186] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-211] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-63] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-103] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-149] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-219] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-43] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [128-133] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [20-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-77] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [118-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-181] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-211] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-194] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-200] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-261] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-205] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.