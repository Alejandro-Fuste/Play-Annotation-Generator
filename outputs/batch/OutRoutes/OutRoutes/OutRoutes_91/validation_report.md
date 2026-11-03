# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_91`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
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
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [107-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-78] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-93] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-64] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-20] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-93] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-86] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [108-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-20] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.