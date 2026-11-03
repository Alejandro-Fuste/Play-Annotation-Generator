# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_3`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 7: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [26–42], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=43.
> - Action 'Action_None' range [26-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-38] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-88] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [89-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-218] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-220] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [128-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-53] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-110] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-187] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-211] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-230] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '30' has 1 frames without a visible bounding box.
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