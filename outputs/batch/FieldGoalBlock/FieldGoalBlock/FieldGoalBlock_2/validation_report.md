# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_2`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 5: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [0-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-41] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-86] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-106] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-49] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-63] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [43-56] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [0-92] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-46] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-111] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-111] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [14-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-23] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-5] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-99] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-14] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-99] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-99] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-18] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-41] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-52] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-58] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-83] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.