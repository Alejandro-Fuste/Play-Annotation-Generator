# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_146`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_146/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 294: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 92 frames exceeds threshold 90 frames [start=142, end=233].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 92 frames exceeds threshold 90 frames [start=142, end=233].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 92 frames exceeds threshold 90 frames [start=142, end=233].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (C) duration 92 frames exceeds threshold 90 frames [start=142, end=233].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [139–151], lower_priority='Action_ZoneBlock' annotated_start=142, effective_Action_ZoneBlock_start=152.
> - Action 'Action_SplitBlock' range [143-159] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [214-220] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-241] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-288] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [157-277] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-248] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-264] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-355] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-274] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-174] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [176-182] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [208-217] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-274] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [177-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-245] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-221] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-254] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-256] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-277] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-251] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-359] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-351] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-342] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-342] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-340] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-351] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [341-346] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-359] for track '34' has 2 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.