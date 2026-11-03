# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_13`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 18: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 18: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_RunAfterCatch' range [96-126] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [129-131] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [138-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [143-150] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-122] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-150] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [25-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-82] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-93] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-119] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-95] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [102-150] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-47] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-47] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-75] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [79-150] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-57] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-63] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-64] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-104] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-119] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-141] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-150] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '27' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.