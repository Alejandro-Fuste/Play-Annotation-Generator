# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_79`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 155 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [31–49], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=50.
> - Action 'Action_None' range [31-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-229] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-63] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-73] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-82] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-100] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-242] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-98] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-110] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-156] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-263] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-82] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [31-142] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-249] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-85] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-70] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [69-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [31-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-78] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 106, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [106-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-51] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-58] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-269] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-140] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-105] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-247] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-258] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-223] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-242] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-249] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-246] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-259] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-199] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-236] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-153] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-202] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-214] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-179] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-194] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-246] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-260] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-199] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-242] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-256] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-244] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [256-266] for track '35' has 2 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.