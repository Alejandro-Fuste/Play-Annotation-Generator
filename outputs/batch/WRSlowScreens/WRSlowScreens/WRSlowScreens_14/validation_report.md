# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_14`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_14/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [16–31], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=32.
> - Action 'Action_None' range [16-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-178] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-36] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-207] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-184] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [117-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [196-216] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-239] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-217] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '26' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.