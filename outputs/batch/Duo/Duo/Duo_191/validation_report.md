# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_191`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_191/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-124] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-142] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-148] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-103] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-118] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-147] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-150] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [84-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-139] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [84-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [89-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [104-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [107-112] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-150] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-139] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-150] for track '30' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.