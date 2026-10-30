# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `FieldGoalBlock_117`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_117/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BlockKick' at frame 56 targets track ID '-', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [52-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-126] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-147] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-73] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-112] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-54] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-150] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-51] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-62] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-78] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-95] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-150] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-51] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [53-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-60] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-150] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-76] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [82-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-58] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-94] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-138] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-45] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-60] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-150] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-131] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-141] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-142] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.