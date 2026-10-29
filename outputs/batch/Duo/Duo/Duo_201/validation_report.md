# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_201`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_201/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 60 |
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
> - Action 'Action_PreSnap' range [115-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-148] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [58-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [58-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [65-89] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [58-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [77-89] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-112] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-92] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-132] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-150] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-64] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-125] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-114] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-150] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-150] for track '25' has 1 frames without a visible bounding box.
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
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.