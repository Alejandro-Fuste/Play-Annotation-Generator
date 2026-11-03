# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_113`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_113/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
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
> - Action 'Action_PreSnap' range [0-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [98-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [147-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [153-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [98-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-24] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-48] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-77] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-134] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-58] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-127] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-172] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '31' has 1 frames without a visible bounding box.
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