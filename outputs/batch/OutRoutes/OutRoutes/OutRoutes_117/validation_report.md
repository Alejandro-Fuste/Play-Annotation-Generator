# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_117`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_117/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 69 |
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
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [47-147] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-197] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-205] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-112] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-128] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-106] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-209] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-93] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-207] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-94] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-132] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [134-142] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [144-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-167] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-64] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-210] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-172] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-210] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-187] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-206] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.