# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_7`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 16: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [7-155] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-152] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-47] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-50] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-84] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-40] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [66-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [176-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-37] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-99] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [106-152] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-67] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-85] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-77] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [7-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [76-77] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '31' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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