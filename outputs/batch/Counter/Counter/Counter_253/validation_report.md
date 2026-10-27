# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_253`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_253/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 508: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [168–187], lower_priority='Action_DownBlock' annotated_start=171, effective_Action_DownBlock_start=188.
> - Overlapping action conflict at frame 187 for track '18': 'Action_SnapReceive' vs 'Action_Handoff'. Overriding with 'Action_Handoff'.
> - Action 'Action_None' range [168-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-254] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-261] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [175-338] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-209] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-233] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-355] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-352] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [188-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [199-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-349] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-240] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-274] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [187-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-333] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-356] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-224] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-355] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-344] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-48] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-283] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-275] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '26' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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