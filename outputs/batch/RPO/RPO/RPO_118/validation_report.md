# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_118`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_118/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [61-115] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-147] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [62-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [96-105] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [62-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [71-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [92-107] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [114-120] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-89] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-179] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PullBall' range [75-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-146] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-78] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [62-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [79-84] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [62-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [85-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-30] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [62-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [98-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-142] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-172] for track '23' has 1 frames without a visible bounding box.
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