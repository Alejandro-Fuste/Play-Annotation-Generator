# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_27`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 32: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [7-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-48] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [69-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-35] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-49] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [23-147] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-50] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-87] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-139] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-180] for track '22' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.