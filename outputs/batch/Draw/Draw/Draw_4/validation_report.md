# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_4`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 32 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
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
> - Segment 'Action_BallCarry' for track '9' has invalid range: start=64, end=52. Clamping end to start.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [20–40], lower_priority='Action_PassBlock' annotated_start=23, effective_Action_PassBlock_start=41.
> - Action 'Action_None' range [20-68] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-91] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [93-109] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-52] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-31] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 20, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [20-20] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-29] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-34] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-102] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [20-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [46-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-33] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-207] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-109] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-134] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-198] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-203] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-208] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '25' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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