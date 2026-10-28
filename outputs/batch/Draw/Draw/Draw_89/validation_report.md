# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_89`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [32–47], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=48.
> - Action 'Action_None' range [32-145] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-126] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-45] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [53-58] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [63-65] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [69-88] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-88] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-179] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-239] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-35] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-50] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [32-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [48-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-80] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [86-94] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 100, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [100-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-239] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-145] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-212] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-226] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '30' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.