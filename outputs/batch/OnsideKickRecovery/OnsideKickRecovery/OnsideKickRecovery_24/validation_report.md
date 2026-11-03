# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_24`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [3-73] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-105] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-100] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [99-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' for track '5' starts at frame 150, but the player has no visible bounding box on this frame.
> - Action 'Action_SecureRecovery' range [150-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [152-173] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [182-185] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [3-16] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [32-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-117] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-94] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-126] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-22] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-100] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-194] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-209] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '35' has 1 frames without a visible bounding box.
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