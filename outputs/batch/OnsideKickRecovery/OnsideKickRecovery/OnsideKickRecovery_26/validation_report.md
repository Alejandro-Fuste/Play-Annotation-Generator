# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_26`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_26/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_AttemptRecovery' for track '17' has invalid range: start=94, end=92. Clamping end to start.
> - Segment 'Action_SecureRecovery' for track '17' has invalid range: start=102, end=92. Clamping end to start.
> - Action 'Action_None' range [3-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [50-94] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [96-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-64] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-143] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-127] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-139] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-20] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-161] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-85] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-24] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-33] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-13] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-16] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-27] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-10] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-15] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-66] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-17] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-34] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-105] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [108-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-34] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-99] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-61] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-132] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-119] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-116] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-105] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-129] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-138] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-131] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '35' has 1 frames without a visible bounding box.
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