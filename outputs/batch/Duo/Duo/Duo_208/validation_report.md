# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_208`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_208/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BlockSecondLevel' for track '8' has invalid range: start=70, end=68. Clamping end to start.
> - Action 'Action_PreSnap' range [0-12] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-88] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' for track '4' starts at frame 57, but the player has no visible bounding box on this frame.
> - Action 'Action_ComboBlock' range [57-61] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [64-76] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [81-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-28] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-50] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [66-67] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [57-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [64-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-11] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-109] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-150] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-86] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-141] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-82] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-94] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-39] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-115] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-150] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.