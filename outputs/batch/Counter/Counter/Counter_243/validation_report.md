# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_243`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_243/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 487: Duplicate assignment for track ID '22' in grid. Overwriting previous assignment.
> - Row 487: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - Row 488: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 488: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [177–191], lower_priority='Action_DownBlock' annotated_start=181, effective_Action_DownBlock_start=192.
> - Segment 'Action_BallCarry' for track '21' has invalid range: start=221, end=211. Clamping end to start.
> - Action 'Action_None' range [177-283] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-449] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [181-264] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-252] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-434] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-439] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-264] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-327] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-286] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-326] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [208-233] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [236-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-199] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-420] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [181-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-194] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [198-204] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [206-211] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [192-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-312] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-318] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-340] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-346] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-399] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-273] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-295] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-335] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-412] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-449] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-449] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-393] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-402] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-422] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-435] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-438] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-444] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-427] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-434] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-445] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-432] for track '38' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.