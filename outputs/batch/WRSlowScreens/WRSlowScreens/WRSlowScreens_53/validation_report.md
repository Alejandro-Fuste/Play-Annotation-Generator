# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_53`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
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
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [4–20], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=21.
> - Action 'Action_None' range [4-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-199] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [100-177] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [181-183] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-25] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [45-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-182] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-182] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-153] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-43] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '26' has 1 frames without a visible bounding box.
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