# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_13`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 28: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [49-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-150] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [49-130] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-130] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-79] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 49, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [49-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-150] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-150] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-33] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-150] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-74] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-91] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-150] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-146] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-134] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-118] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-144] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '33' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.