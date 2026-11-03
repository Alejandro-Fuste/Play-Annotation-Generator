# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_57`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_57/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 62: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [81-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [136-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [147-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-150] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-21] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-68] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.