# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_39`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 42: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [2–18], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=19.
> - Action 'Action_None' range [2-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [18-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-60] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-124] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-20] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [79-119] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-157] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-61] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-9] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-14] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-26] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-32] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-145] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.