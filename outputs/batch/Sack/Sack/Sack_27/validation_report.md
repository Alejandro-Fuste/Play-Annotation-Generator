# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_27`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 39 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 29, Column 'Wrap Quarterback': Unknown actor track ID '?' in entry '87,?'.
> - Row 29, Column 'Sack Quarterback': Single text entry '?' could not be parsed as a frame number.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-90] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-90] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-90] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [70-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-90] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-90] for track '24' has 1 frames without a visible bounding box.
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