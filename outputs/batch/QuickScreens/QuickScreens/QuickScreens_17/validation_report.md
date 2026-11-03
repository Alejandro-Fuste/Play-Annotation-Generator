# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_17`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 22: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_ScreenBlock' range [15-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [86-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [97-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-131] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-48] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-150] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [16-22] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-28] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-148] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [66-132] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-135] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-39] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-37] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-48] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-60] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-44] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [2-138] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-38] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-97] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-38] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-39] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-89] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-139] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-143] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '36' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.