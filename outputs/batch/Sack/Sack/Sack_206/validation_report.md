# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_206`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_206/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 208, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '134,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-109] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-96] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-122] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [105-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [112-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [123-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-95] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [105-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-113] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-87] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-110] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-150] for track '23' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.