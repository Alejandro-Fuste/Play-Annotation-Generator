# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_37`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 39, Column 'Close On Quarterback': Unknown actor track ID '?' in entry '90,?'.
> - Row 39, Column 'Wrap Quarterback': Unknown actor track ID '?' in entry '120,?'.
> - Row 39, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '128,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-68] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-91] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-99] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-142] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-100] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-93] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-114] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-68] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-86] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-150] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-147] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-150] for track '25' has 1 frames without a visible bounding box.
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