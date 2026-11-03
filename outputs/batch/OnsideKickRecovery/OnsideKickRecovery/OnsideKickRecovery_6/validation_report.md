# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_6`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [4-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-170] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-137] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-133] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-156] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [69-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [125-148] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-121] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-168] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-113] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-122] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-77] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-151] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' for track '19' starts at frame 155, but the player has no visible bounding box on this frame.
> - Action 'Action_SecureRecovery' range [155-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-96] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-180] for track '22' has 1 frames without a visible bounding box.
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