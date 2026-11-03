# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_21`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 34: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 34: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 34: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [15–29], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=30.
> - Action 'Action_SellRoute' range [58-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [102-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-127] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-111] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-121] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-101] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-156] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-119] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-96] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-131] for track '23' has 2 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.