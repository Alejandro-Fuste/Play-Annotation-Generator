# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_68`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_68/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '10' has invalid range: start=69, end=6. Clamping end to start.
> - Action 'Action_PreSnap' range [0-113] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-123] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-134] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-147] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [69-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-92] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-17] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-25] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-49] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-122] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-149] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-119] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-61] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-149] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '22' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.