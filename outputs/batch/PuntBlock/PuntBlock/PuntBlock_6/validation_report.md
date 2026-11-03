# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_6`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 14: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [2-202] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-51] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-213] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [143-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [175-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [182-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [194-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [206-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [63-71] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-79] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [57-199] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-43] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-57] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-39] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-168] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-22] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-23] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-140] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-199] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-217] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-53] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-129] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '34' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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