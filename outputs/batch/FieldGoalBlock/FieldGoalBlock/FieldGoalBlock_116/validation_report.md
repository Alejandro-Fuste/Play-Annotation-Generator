# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_116`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_116/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [31-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-53] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-78] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-44] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-31] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [37-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [47-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-90] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-76] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-81] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-82] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-90] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-17] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-84] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-63] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-90] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [72-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-90] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-90] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.