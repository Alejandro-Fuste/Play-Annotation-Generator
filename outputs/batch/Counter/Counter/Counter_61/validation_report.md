# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_61`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 124: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 124: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [127–148], lower_priority='Action_DownBlock' annotated_start=132, effective_Action_DownBlock_start=149.
> - Action 'Action_None' range [127-219] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-260] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-198] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [132-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-246] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-254] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-266] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-269] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-252] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [254-255] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-256] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [149-163] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [165-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [168-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [175-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-267] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [132-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [156-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [132-212] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-230] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-252] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '27' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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