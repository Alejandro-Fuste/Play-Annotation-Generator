# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_64`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '14' has invalid range: start=73, end=64. Clamping end to start.
> - Action 'Action_PreSnap' range [0-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-149] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [73-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [78-135] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-129] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-149] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-149] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-91] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-149] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [74-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [87-90] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-21] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-45] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-9] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-59] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-133] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-149] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-149] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-148] for track '22' has 2 frames without a visible bounding box.
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