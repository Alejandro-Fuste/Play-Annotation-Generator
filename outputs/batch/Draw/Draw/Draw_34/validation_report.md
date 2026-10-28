# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_34`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [19–39], lower_priority='Action_PassBlock' annotated_start=22, effective_Action_PassBlock_start=40.
> - Action 'Action_None' range [19-109] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-71] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-226] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-62] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [68-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-236] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-46] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-190] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-224] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-104] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-63] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-234] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-156] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-197] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-229] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-237] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.