# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_13`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 28: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [50–103], lower_priority='Action_PullBlock' annotated_start=103, effective_Action_PullBlock_start=104.
> - Action 'Action_None' range [50-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-233] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-209] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-228] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [50-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [104-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '27' has 1 frames without a visible bounding box.
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