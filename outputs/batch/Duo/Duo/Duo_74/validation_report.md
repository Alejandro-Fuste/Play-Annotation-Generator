# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_74`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_74/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 42 |
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
> - Action 'Action_ComboBlock' range [45-71] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [77-86] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-79] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-119] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [45-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [76-82] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-106] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-79] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-100] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-62] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-64] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-119] for track '20' has 1 frames without a visible bounding box.
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