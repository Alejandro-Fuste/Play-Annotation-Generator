# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_113`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_113/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 228: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [38-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-69] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [45-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-42] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-23] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-46] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-90] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-90] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '26' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.