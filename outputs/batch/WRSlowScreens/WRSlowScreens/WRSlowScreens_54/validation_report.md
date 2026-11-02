# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_54`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_ReleaseToScreen' range [29-36] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-75] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-20] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-36] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-6] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-58] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-73] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-13] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-37] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [1-6] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-11] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-30] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [1-4] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-18] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-55] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-147] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-58] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-147] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [87-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [137-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '26' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.