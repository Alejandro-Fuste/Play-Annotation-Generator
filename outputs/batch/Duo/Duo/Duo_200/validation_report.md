# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_200`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_200/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '20' has invalid range: start=84, end=82. Clamping end to start.
> - Action 'Action_PreSnap' range [0-105] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-154] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-175] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-150] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [84-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-123] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [84-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-175] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [84-92] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [95-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [99-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-175] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-159] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-160] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-175] for track '29' has 3 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.