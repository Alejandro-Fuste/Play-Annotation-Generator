# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_27`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 56: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_None' range [97-214] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-268] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-22] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-174] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-229] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [231-268] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-263] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-268] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-189] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [191-221] for track '6' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-153] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-175] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-22] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '9' starts at frame 141, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [141-153] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [155-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [250-252] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-96] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-172] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-214] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-261] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [100-152] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [155-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [161-175] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [178-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [181-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-268] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-158] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-245] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-268] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-12] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-174] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-213] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [100-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [177-186] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-17] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-34] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-96] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-268] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-229] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-268] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-217] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-221] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [192-218] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-211] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [195-221] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-268] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-268] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-263] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.