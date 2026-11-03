# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_23`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
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
> - Segment 'Action_SecureRecovery' for track '14' has invalid range: start=141, end=102. Clamping end to start.
> - Action 'Action_None' range [7-87] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-113] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-113] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-176] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-69] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 7, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [7-7] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [30-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-78] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [96-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-180] for track '15' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [7-46] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-23] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-139] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-180] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [68-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-130] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-167] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-176] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '30' has 1 frames without a visible bounding box.
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