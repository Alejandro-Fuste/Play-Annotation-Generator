# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_17`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [64–78], lower_priority='Action_DownBlock' annotated_start=62, effective_Action_DownBlock_start=79.
> - Action 'Action_None' range [64-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-141] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-164] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-81] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [85-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-112] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [70-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [113-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [137-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-124] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-157] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-181] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [112-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [64-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [62-84] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [90-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [100-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-163] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-192] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.