# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_39`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 28: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [70–85], lower_priority='Action_PassBlock' annotated_start=73, effective_Action_PassBlock_start=86.
> - Action 'Action_None' range [70-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-272] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-216] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [172-285] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [70-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [86-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-265] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-299] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-236] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-260] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-285] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [164-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [172-250] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-115] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-276] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [279-299] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-295] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-291] for track '24' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.