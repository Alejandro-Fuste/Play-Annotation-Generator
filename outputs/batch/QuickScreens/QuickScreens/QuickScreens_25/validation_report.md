# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_25`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_ScreenBlock' range [38-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [93-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [135-138] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-57] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-60] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-105] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-65] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-85] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-87] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-159] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-141] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-60] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-53] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-75] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-89] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-49] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-155] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-114] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-127] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-170] for track '29' has 2 frames without a visible bounding box.
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