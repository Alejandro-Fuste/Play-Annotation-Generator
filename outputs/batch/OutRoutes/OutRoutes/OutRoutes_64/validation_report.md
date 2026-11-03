# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_64`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 45 |
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
> - Segment 'Action_BallCarry' for track '0' has invalid range: start=82, end=78. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '18' has invalid range: start=137, end=11. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '18' has invalid range: start=137, end=48. Clamping end to start.
> - Action 'Action_SecureCatch' range [75-78] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [11-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-9] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-17] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-61] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-104] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [107-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-11] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-16] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [79-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-178] for track '23' has 1 frames without a visible bounding box.
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