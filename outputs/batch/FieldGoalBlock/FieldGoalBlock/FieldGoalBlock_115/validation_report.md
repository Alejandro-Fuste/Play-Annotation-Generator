# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `FieldGoalBlock_115`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_115/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BlockKick' at frame 51 targets track ID '-', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 232: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 232: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [47-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 47, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [47-51] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-45] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-46] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-40] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-49] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-89] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PlaceBall' range [23-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-120] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-57] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-72] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-21] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-42] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-120] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-90] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-120] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-119] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '26' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.