# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_18`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_18/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 37: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SecureRecovery' for track '14' has invalid range: start=115, end=109. Clamping end to start.
> - Action 'Action_None' range [2-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-36] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-123] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-148] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-56] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-84] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-95] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-71] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-34] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-50] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-56] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-102] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [109-123] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-100] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-65] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-56] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-150] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [2-18] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [20-30] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_KickBall' range [48-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [57-65] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_KickBall' range [70-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [86-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [100-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [106-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-20] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-4] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-81] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-81] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-106] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [108-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-123] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-112] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-150] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-116] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-108] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-98] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-138] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-150] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.