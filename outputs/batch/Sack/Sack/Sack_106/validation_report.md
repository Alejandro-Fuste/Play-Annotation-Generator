# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_106`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 18 |
| Player Tracks | 18 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 36 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-89] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-79] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-79] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [88-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-119] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [60-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [63-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [74-83] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-119] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-117] for track '17' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.