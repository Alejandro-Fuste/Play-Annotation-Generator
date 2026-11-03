# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_5`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_AttemptRecovery' for track '13' has invalid range: start=105, end=98. Clamping end to start.
> - Action 'Action_None' range [1-145] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [1-54] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [55-83] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [86-88] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [96-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [118-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-127] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-134] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-118] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-53] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-10] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-107] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [136-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [141-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-168] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-170] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.