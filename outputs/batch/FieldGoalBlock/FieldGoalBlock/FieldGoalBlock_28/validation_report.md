# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_28`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_28/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 58: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 58: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
> - Row 58: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 58: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 58: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [29-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-178] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-126] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-135] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-61] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-147] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-177] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-180] for track '10' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [29-65] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-52] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-52] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-72] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-68] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-42] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-37] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-42] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-141] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-20] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' for track '21' starts at frame 71, but the player has no visible bounding box on this frame.
> - Action 'Action_BlockKick' range [71-76] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-180] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '31' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.