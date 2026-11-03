# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_17`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 49 |
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
> - Action 'Action_PreSnap' range [0-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-130] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [143-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [124-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-117] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [120-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-180] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-60] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-161] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-176] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-144] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-174] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-176] for track '26' has 1 frames without a visible bounding box.
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