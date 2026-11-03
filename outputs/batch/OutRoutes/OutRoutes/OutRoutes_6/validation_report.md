# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_6`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 60 |
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
> - Action 'Action_PreSnap' range [0-150] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-105] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-45] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-100] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [143-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [156-157] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [159-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [24-70] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-125] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-24] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-117] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-125] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [95-155] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [161-180] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-148] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-180] for track '25' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.