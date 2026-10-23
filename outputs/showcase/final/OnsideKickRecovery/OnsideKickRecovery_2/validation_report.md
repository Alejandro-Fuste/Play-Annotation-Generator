# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_2`
- **Input XML**: `output_showcase_final/OnsideKickRecovery/OnsideKickRecovery_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 5: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [23-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-133] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [132-146] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [150-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-134] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-160] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [110-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [125-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [164-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [177-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [52-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-65] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-77] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-18] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-34] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-13] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-27] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-41] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-163] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '35' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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