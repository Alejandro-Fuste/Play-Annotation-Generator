# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_183`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_183/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-113] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-118] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [75-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-125] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-81] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [75-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [75-93] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [75-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-125] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-13] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-125] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-115] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-108] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-125] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-125] for track '24' has 1 frames without a visible bounding box.
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
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.