# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_91`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 96: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 96: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-99] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [6-69] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [51-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [94-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-29] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-116] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-69] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-120] for track '23' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.