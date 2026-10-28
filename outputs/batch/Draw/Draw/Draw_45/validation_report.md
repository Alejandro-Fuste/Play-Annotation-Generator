# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_45`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 90: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [39–56], lower_priority='Action_PassBlock' annotated_start=42, effective_Action_PassBlock_start=57.
> - Action 'Action_None' range [39-76] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-104] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-132] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [39-83] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-82] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-166] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [39-48] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [50-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-198] for track '27' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.