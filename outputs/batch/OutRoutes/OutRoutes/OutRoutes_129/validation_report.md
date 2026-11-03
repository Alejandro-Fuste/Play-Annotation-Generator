# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_129`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 61 |
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
> - Action 'Action_PreSnap' range [0-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [135-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-40] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-26] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-20] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-44] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-14] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-70] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-117] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '31' has 1 frames without a visible bounding box.
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