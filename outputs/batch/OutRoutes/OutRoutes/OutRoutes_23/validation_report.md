# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_23`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 59 |
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
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [142-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-82] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-88] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-150] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-52] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-73] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [90-150] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-52] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-71] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-150] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-98] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-110] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-150] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.