# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_147`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_147/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [117-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-139] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-62] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-79] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-107] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-85] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-139] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-121] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [130-132] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [142-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-26] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-61] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-99] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-124] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-129] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-150] for track '26' has 1 frames without a visible bounding box.
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
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.