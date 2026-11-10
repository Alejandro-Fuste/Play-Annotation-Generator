# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_182`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_182/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 184, Column 'Close On Quarterback': Unknown actor track ID '?' in entry '75,?'.
> - Row 184, Column 'Wrap Quarterback': Unknown actor track ID '?' in entry '102,?'.
> - Row 184, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '115,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-120] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-86] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-62] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-59] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-120] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-60] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-117] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '26' has 1 frames without a visible bounding box.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.