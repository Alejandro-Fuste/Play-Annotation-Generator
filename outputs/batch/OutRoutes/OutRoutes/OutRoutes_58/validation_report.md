# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_58`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_58/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 42 |
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
> - Segment 'Action_SecureCatch' for track '4' has invalid range: start=101, end=68. Clamping end to start.
> - Segment 'Action_BallCarry' for track '4' has invalid range: start=109, end=68. Clamping end to start.
> - Segment 'Action_PassBlock' for track '8' has invalid range: start=21, end=11. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '10' has invalid range: start=70, end=57. Clamping end to start.
> - Action 'Action_PreSnap' range [0-81] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-81] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [27-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-44] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-28] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-70] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-57] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-67] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-73] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-47] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-71] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-51] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-120] for track '20' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.