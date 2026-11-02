# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_42`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_42/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [13–31], lower_priority='Action_PassBlock' annotated_start=16, effective_Action_PassBlock_start=32.
> - Action 'Action_None' range [13-53] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-35] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [156-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-132] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-47] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [44-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [55-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-180] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-36] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-112] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-26] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-33] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-173] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-119] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [107-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [157-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-171] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '29' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.