# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_67`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 69, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '170,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-170] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-151] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [150-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-148] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-173] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [129-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '18' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-115] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-168] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.