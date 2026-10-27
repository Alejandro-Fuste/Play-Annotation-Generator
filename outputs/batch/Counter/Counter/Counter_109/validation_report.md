# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_109`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 220: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 220: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 220: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [87–100], lower_priority='Action_PullBlock' annotated_start=89, effective_Action_PullBlock_start=101.
> - Action 'Action_None' range [177-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-126] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [87-142] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [146-148] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [150-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [166-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-233] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [139-239] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-215] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-229] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-205] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-190] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-239] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [101-146] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [148-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [158-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [172-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-226] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '24' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.