# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_151`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_151/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 49 |
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
> - Action 'Action_BallCarry' range [87-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-65] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-135] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '26' has 1 frames without a visible bounding box.
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