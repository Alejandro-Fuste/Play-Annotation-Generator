# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_69`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [25–42], lower_priority='Action_DownBlock' annotated_start=28, effective_Action_DownBlock_start=43.
> - Action 'Action_None' range [25-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-232] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-74] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-78] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-99] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [25-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-93] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-218] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [78-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [28-77] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-95] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [28-45] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [49-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [59-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [67-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [28-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-107] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-143] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-140] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-130] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-175] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-181] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-171] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-203] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.