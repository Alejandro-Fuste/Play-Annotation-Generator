# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_36`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 74: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [13-90] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [74-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-45] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-38] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-19] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-23] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-53] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-54] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-90] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-90] for track '26' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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