# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_1`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 39 |
| Ball Tracks | 6 |
| CSV events parsed | 22 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Overlapping action conflict at frame 20 for track '11': 'Action_SnapReceive' vs 'Action_RunDeepCrossRoute'. Overriding with 'Action_RunDeepCrossRoute'.
> - Action 'Action_None' range [6-166] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-202] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-25] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-155] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-117] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-131] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [125-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [138-150] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-168] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [6-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [136-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [158-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [166-171] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-21] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-100] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-166] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-69] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-172] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-91] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-119] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-167] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-220] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-192] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-146] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-163] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-201] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-269] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-269] for track '43' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
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