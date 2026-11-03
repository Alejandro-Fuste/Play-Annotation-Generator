# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_5`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 10: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [11–23], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=24.
> - Action 'Action_None' range [11-245] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-39] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-55] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [84-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-92] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-126] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-124] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [108-109] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-148] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-132] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [108-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [115-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [105-106] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-192] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-237] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-240] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-245] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-245] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [249-252] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-164] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [167-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [174-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [182-198] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [200-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-245] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-72] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-243] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-185] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-205] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-250] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-249] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-261] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '41' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.