# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_49`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 43 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 51, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '120,135;?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 100: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 100: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [101-114] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [118-145] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [147-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-74] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-139] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-150] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-150] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-46] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-85] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-150] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-83] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-88] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-100] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-114] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-150] for track '21' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.