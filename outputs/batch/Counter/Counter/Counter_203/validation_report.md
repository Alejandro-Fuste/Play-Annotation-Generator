# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_203`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_203/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 408: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [141–153], lower_priority='Action_DownBlock' annotated_start=144, effective_Action_DownBlock_start=154.
> - Validation warning: Action 'Action_DownBlock' for track '18' (RT) duration 103 frames exceeds threshold 90 frames [start=144, end=246].
> - Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 103 frames exceeds threshold 90 frames [start=144, end=246].
> - Action 'Action_None' range [141-282] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-305] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-214] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-258] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-183] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-239] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-270] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-235] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-250] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-335] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [348-350] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-309] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [191-243] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-270] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-359] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-226] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [170-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-297] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-292] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [154-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [164-171] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-173] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [176-198] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [144-237] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-166] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [170-181] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [144-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-275] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-351] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-257] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-250] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-300] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-359] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-325] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-352] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '31' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.