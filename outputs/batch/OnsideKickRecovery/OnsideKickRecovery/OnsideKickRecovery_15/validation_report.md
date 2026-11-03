# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_15`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 128 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 32: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_AttemptRecovery' range [129-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-201] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-126] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-80] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-144] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [157-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-62] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-84] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-113] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-167] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-30] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-83] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [2-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [26-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [43-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-114] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-92] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-5] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-156] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-14] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-15] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-28] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-13] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-204] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [46-70] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [73-100] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [110-152] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-93] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-154] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-73] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-130] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [133-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-77] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-87] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-124] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-159] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-178] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-187] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-192] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-208] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-209] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '43' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.