# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_46`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 54: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-74] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [17-68] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [80-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-64] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-137] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-50] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-68] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [94-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-47] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-89] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-65] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-67] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-86] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-83] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-110] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '28' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.