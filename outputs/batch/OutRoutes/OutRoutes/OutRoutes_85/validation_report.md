# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_85`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 67 |
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
> - Action 'Action_RunOutRoute' range [21-56] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [59-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-134] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-165] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-139] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-69] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-47] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-81] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-100] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-135] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-51] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-60] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-30] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [48-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [86-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-71] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-58] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-140] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-127] for track '25' has 1 frames without a visible bounding box.
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