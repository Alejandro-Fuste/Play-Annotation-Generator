# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_83`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 166: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [3–19], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=20.
> - Action 'Action_None' range [3-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-48] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-43] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [50-230] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-8] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-13] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-50] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-212] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-213] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-191] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '28' has 1 frames without a visible bounding box.
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