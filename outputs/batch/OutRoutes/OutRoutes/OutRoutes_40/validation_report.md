# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_40`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 38 |
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
> - Segment 'Action_ThrowPass' for track '8' has invalid range: start=121, end=88. Clamping end to start.
> - Segment 'Action_SecureCatch' for track '25' has invalid range: start=156, end=149. Clamping end to start.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-113] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-111] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [37-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-88] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-164] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [156-180] for track '25' has 1 frames without a visible bounding box.
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
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.