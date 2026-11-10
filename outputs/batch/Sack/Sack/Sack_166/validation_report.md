# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_166`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_166/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 55 |
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
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-82] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-105] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-106] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [94-105] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [112-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [77-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-120] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.