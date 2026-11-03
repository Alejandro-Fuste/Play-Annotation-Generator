# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_63`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [12–26], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=27.
> - Action 'Action_None' range [12-171] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [12-103] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [108-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-178] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [190-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-181] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-201] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-69] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-48] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-69] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-45] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-55] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-69] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-110] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [12-87] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [66-76] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 77, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [77-151] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [12-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-169] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-36] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-69] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-48] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-168] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-68] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-107] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [109-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-159] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-69] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-114] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [120-153] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-32] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-69] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-87] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-103] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-124] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-69] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-141] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '29' has 5 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.