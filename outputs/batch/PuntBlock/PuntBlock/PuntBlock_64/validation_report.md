# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_64`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 62 |
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
> - Action 'Action_None' range [28-74] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-105] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-120] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-204] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-103] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-95] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [78-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [114-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-46] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-149] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.