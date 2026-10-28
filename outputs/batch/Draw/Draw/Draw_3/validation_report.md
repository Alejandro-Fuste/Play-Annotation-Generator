# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_3`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 157 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [64–83], lower_priority='Action_PassBlock' annotated_start=67, effective_Action_PassBlock_start=84.
> - Action 'Action_None' range [64-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-269] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-221] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-243] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-231] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-251] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-205] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-269] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-166] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-230] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-269] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-231] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-167] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-212] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-251] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-252] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-110] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-136] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-97] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-216] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-240] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-250] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '17' starts at frame 84, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [84-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-103] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-166] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [168-185] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-159] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-252] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-262] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-163] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-110] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-169] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-216] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-237] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-252] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-262] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-230] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-251] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-261] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-246] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-263] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-252] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '35' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.