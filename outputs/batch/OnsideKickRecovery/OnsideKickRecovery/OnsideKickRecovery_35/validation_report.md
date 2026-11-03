# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_35`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [2-220] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-194] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-228] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-83] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-204] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [157-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [216-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-148] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-151] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-216] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-235] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-147] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-175] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-199] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [77-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [125-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-141] for track '15' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-5] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-30] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-56] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-232] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-103] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-114] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-198] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-203] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [193-201] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [204-219] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.