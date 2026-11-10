# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_169`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_169/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-103] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-108] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [99-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-106] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-85] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [85-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [117-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-113] for track '21' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.