# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_272`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_272/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [37–51], lower_priority='Action_DownBlock' annotated_start=40, effective_Action_DownBlock_start=52.
> - Action 'Action_None' range [37-103] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [40-67] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [40-64] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [71-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [78-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-48] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-52] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-57] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-67] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-115] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-64] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [40-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-65] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [40-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [73-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [52-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [64-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-53] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [37-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-31] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-104] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [46-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-92] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-156] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-167] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '34' has 1 frames without a visible bounding box.
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