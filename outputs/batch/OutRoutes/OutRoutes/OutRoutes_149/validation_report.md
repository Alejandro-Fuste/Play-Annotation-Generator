# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_149`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_149/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 154: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-31] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-120] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-47] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-16] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-37] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-120] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '23' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.