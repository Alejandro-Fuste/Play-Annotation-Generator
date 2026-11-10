# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_211`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_211/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 34 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-120] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-56] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [91-107] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [109-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [117-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-88] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-107] for track '20' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.