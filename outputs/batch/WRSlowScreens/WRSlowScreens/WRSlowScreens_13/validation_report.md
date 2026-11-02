# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_13`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 8: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [13-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-204] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-194] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [55-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [190-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-109] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-165] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [169-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [117-166] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [175-178] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [181-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-27] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [178-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-33] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '27' has 1 frames without a visible bounding box.
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