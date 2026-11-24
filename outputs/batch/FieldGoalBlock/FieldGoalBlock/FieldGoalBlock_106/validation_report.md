# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_106`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 213: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - Row 214: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [70-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-78] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-61] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-120] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-57] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [84-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-113] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-101] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-120] for track '23' has 3 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Metadata: no Dataset Summary row found for output_file 'FieldGoalBlock_106'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.