# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_79`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 58 |
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
> - Action 'Action_PreSnap' range [0-150] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-52] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [52-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [143-150] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-96] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-150] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-150] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-105] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-131] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '28' has 1 frames without a visible bounding box.
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