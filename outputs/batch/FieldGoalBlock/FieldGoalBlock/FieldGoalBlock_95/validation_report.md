# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `FieldGoalBlock_95`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BlockKick' at frame 38 targets track ID '-', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 192: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [32-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-61] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-75] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-68] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-76] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-50] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-64] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-70] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-55] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-57] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 32, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [32-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-62] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-54] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-11] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-22] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-65] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '23' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.