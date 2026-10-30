# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_17`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 5 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 36: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 36: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 36: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 36: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 36: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 36: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - Row 36: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-26] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-39] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-13] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [32-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-21] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-66] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-53] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-90] for track '23' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.