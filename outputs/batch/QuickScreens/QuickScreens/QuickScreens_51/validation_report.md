# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `QuickScreens_51`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_ScreenBlock' at frame 19 targets track ID '73', but it is not found in XML.
> - Event 'Action_ScreenBlock' at frame 19 targets track ID '92', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 56: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [19-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [50-94] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [99-150] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-129] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-65] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-106] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-117] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '27' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.