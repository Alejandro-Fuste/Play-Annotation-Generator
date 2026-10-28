# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_85`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [32–45], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=46.
> - Action 'Action_PassBlock' range [35-87] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-146] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-139] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [86-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [224-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [32-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-197] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-116] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-146] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-192] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-193] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-195] for track '21' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.