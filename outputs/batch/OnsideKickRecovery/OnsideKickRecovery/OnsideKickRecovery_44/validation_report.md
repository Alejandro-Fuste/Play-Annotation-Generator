# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_44`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
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
> - Action 'Action_None' range [5-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [75-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [138-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-12] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-83] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [89-93] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-103] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-146] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-129] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-145] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-120] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-146] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '21' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.