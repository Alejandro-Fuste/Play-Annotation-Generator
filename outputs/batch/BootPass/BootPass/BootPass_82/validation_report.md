# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_82`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 34 |
| Ball Tracks | 1 |
| CSV events parsed | 21 |
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
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [44–61], lower_priority='Action_RunBlock' annotated_start=51, effective_Action_RunBlock_start=62.
> - Action 'Action_None' range [44-92] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-85] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [51-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [81-139] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [141-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-138] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-143] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [51-64] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [66-86] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [91-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [51-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [108-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [51-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [80-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [88-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [62-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [73-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-62] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-58] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-139] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-119] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-167] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-163] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-208] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '34' has 1 frames without a visible bounding box.
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