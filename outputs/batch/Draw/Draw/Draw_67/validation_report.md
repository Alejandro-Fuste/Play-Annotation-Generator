# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_67`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 137 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 134: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 134: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [26–40], lower_priority='Action_PassBlock' annotated_start=29, effective_Action_PassBlock_start=41.
> - Action 'Action_None' range [26-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-197] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-110] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-120] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-153] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-151] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-204] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-218] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-213] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [78-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-194] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-110] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-157] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-213] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-225] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [26-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [32-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [38-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-70] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-105] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-122] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-211] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-81] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-211] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-197] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-211] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-212] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-227] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-183] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-201] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-218] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-229] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-191] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-187] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-214] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-234] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-234] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-232] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-239] for track '37' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.