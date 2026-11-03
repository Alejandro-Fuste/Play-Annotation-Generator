# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_25`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_AttemptRecovery' for track '22' has invalid range: start=127, end=107. Clamping end to start.
> - Segment 'Action_SecureRecovery' for track '22' has invalid range: start=136, end=107. Clamping end to start.
> - Action 'Action_None' range [35-149] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-103] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [35-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [61-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-220] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-136] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-174] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-136] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-194] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [35-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-24] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-176] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-122] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.