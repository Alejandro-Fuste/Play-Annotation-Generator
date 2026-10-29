# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_187`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_187/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 24 |
| Ball Tracks | 1 |
| CSV events parsed | 14 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-140] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [80-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [107-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [80-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [120-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [80-99] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [107-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [110-114] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [120-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-76] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '24' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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