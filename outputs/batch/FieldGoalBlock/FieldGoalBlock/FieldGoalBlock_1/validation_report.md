# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_1`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 4: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-45] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-53] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-67] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-90] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_KickBall' range [38-39] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_BlockKick' for track '13' starts at frame 40, but the player has no visible bounding box on this frame.
> - Action 'Action_BlockKick' range [40-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-52] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-44] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-52] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-75] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [84-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-90] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-59] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-67] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-18] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-31] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-41] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-59] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-90] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '24' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.