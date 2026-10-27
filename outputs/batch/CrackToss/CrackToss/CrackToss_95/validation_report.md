# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_95`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 145 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 249 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 192: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 192: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '3' (RB2) duration 95 frames exceeds threshold 90 frames [start=123, end=217].
> - Action 'Action_None' range [120-167] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-197] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-242] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-217] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [123-170] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [172-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [177-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [182-197] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [211-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [123-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [174-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [177-197] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [202-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [211-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-241] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-175] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [177-212] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [215-216] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-222] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [224-238] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-10] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-25] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-194] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-249] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-170] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-197] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-21] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-41] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-173] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [175-197] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-230] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-246] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-208] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-217] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-237] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-119] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-144] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-119] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-21] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-119] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-167] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-197] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-45] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [123-168] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [172-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [175-194] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [196-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-49] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-119] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-21] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-45] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-173] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-249] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-119] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-167] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-194] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [132-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-197] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-249] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-236] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-238] for track '30' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.