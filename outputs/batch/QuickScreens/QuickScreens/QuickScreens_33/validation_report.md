# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_33`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_ScreenBlock' range [22-73] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [78-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [64-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-83] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-172] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-105] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-125] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-151] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.