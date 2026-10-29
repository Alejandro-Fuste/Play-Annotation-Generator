# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_162`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_162/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 43 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '15' has invalid range: start=32, end=2. Clamping end to start.
> - Action 'Action_PreSnap' range [0-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-119] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-119] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-119] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-46] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-62] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-69] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-119] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-119] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-102] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '21' has 1 frames without a visible bounding box.
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