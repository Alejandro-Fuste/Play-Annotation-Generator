# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_54`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [43–57], lower_priority='Action_PassBlock' annotated_start=46, effective_Action_PassBlock_start=58.
> - Action 'Action_None' range [43-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-189] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-73] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [83-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-172] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-124] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '18' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.