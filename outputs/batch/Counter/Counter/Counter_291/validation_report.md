# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_291`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_291/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 583: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 584: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '5' (C) duration 100 frames exceeds threshold 90 frames [start=206, end=305].
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [203–215], lower_priority='Action_DownBlock' annotated_start=206, effective_Action_DownBlock_start=216.
> - Validation warning: Action 'Action_DownBlock' for track '17' (Unknown) duration 100 frames exceeds threshold 90 frames [start=206, end=305].
> - Validation warning: Action 'Action_PullBlock' for track '18' (RG) duration 100 frames exceeds threshold 90 frames [start=206, end=305].
> - Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 100 frames exceeds threshold 90 frames [start=206, end=305].
> - Action 'Action_None' range [203-272] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-295] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [216-225] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [227-233] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [242-298] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-411] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-324] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-337] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-385] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-261] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-449] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-291] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-258] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-335] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-273] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-281] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [206-282] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [206-305] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-428] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-446] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [206-229] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [233-246] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [206-286] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-323] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [251-386] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [388-394] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [398-431] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [439-440] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [443-449] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-419] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-410] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-449] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-389] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-407] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-416] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-405] for track '33' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.