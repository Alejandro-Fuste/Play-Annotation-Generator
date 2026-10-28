# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_90`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_90/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [29–43], lower_priority='Action_PassBlock' annotated_start=32, effective_Action_PassBlock_start=44.
> - Action 'Action_None' range [29-258] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [29-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-67] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-103] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-99] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-267] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-194] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-102] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-230] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-92] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-67] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-265] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-218] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-244] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '32' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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