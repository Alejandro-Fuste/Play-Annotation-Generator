# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_54`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 48 |
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
> - Action 'Action_RunOutRoute' range [20-72] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-48] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-69] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-82] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-35] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-76] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [92-145] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [149-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-75] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-81] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-72] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-26] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-143] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-145] for track '23' has 2 frames without a visible bounding box.
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