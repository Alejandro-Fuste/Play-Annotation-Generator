# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_22`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 8 |
| Action Segments inferred | 34 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 24, Column 'Wrap Quarterback': Unknown actor track ID '?' in entry '77,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-103] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [61-71] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [87-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-120] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '23' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.