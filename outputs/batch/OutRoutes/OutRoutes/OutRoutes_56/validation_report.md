# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_56`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 64: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '0' has invalid range: start=86, end=57. Clamping end to start.
> - Segment 'Action_BallCarry' for track '0' has invalid range: start=90, end=57. Clamping end to start.
> - Action 'Action_RunOutRoute' range [20-57] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-80] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-77] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-72] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-64] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-76] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-141] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-92] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-150] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-150] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-147] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '36' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.