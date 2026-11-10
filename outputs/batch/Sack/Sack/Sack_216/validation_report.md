# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_216`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_216/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 43 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 218, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '113,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 434: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [88-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-89] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-117] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-89] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-96] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-117] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-119] for track '24' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.