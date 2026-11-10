# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_157`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_157/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-121] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-116] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-41] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-57] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [98-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [107-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [116-125] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [135-143] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [145-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-73] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-81] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '19' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.