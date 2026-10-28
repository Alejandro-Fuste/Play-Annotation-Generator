# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_43`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
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
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [62–76], lower_priority='Action_PassBlock' annotated_start=65, effective_Action_PassBlock_start=77.
> - Action 'Action_PassBlock' range [65-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-185] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-188] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 135, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [135-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-234] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-121] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-222] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-239] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [62-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-82] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-114] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-91] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-215] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [220-230] for track '26' has 3 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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