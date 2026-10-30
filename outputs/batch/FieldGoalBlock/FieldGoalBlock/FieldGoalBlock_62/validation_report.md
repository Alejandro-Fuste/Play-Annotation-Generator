# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_62`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 126: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [41-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-45] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-116] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-99] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-102] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-24] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-120] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-20] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-43] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-51] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-107] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '29' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.