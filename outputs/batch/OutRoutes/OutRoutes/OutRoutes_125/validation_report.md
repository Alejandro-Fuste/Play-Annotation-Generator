# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_125`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_125/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 132: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 132: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-49] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-93] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-111] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-115] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-128] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-85] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-105] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-56] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-119] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-117] for track '24' has 2 frames without a visible bounding box.
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