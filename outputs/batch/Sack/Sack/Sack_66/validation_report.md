# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_66`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 39 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 68, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '114,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [80-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-30] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-78] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [107-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '21' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.