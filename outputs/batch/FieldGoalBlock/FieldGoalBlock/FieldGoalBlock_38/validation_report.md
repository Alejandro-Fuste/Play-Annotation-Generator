# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_38`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 77: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 78: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [34-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [42-44] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-62] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-120] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-71] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-92] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-118] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '28' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.