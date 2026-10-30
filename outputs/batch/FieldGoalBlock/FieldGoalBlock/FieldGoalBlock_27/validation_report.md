# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_27`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 56: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 56: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 56: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - Row 56: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [62-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [76-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-167] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-58] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 62, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [62-210] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-110] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-82] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-83] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-99] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-132] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-52] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-89] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-55] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-93] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [95-103] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-210] for track '28' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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