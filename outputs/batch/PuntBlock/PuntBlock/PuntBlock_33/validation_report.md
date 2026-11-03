# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_33`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 139 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 68: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [16-205] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-64] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-209] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-223] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-74] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-205] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-220] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-249] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-256] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [142-152] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-149] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [75-92] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [94-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [117-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [130-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [145-202] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [16-34] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-235] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-50] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-243] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-211] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [213-218] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-229] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-69] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-191] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [16-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-136] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-75] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-111] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-143] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [145-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-231] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-252] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-258] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-117] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-184] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-86] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-108] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-133] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-204] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-254] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-199] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-219] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-263] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-215] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-215] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-263] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-269] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '43' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.