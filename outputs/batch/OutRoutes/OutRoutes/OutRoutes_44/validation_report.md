# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_44`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 40 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 52: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '1' has invalid range: start=90, end=68. Clamping end to start.
> - Segment 'Action_BallCarry' for track '1' has invalid range: start=99, end=68. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '14' has invalid range: start=74, end=16. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '14' has invalid range: start=74, end=59. Clamping end to start.
> - Action 'Action_PreSnap' range [0-63] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [16-68] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-72] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-67] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-84] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-92] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-70] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-177] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '23' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.