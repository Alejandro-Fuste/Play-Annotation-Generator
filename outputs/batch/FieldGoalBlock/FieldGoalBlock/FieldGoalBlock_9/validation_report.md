# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_9`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 20: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' for track '0' starts at frame 62, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [62-120] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-99] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-55] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 56, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [56-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-120] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-76] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-85] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-70] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-116] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-49] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-120] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-31] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-45] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-55] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-120] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-120] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-86] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-120] for track '25' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.