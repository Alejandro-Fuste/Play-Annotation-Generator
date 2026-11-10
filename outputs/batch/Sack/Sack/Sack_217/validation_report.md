# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_217`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_217/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 18 |
| Player Tracks | 18 |
| Ball Tracks | 0 |
| CSV events parsed | 8 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 219, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '100,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-79] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-92] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-82] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-105] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-98] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [75-83] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-108] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-83] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-86] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-106] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '17' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.