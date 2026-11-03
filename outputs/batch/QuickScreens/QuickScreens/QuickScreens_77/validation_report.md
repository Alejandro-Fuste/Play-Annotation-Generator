# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_77`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_77/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 82: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [3-103] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [75-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [119-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-30] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-75] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-123] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-152] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-33] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [24-108] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-35] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-80] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-115] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-49] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-31] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-90] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-166] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-141] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-179] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [3-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-38] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-180] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [44-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-79] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-158] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-180] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-169] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-180] for track '29' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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