# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_78`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [27–40], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=41.
> - Action 'Action_None' range [27-45] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-47] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-55] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-39] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-51] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-57] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-190] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-117] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [27-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-162] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [56-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-91] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-202] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-197] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '23' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.