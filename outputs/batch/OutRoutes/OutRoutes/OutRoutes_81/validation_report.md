# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_81`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_81/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 88: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 88: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [27-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-176] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [176-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-59] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-90] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-160] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-168] for track '30' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.