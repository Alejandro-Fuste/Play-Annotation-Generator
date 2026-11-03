# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_37`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 44 |
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
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [4-46] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [51-52] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [54-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [111-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-120] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-12] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-42] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-71] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.