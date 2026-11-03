# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_25`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 38: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 38: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 38: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [2–17], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=18.
> - Action 'Action_None' range [2-118] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-187] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-312] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-43] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-139] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-301] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-307] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-328] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-184] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-193] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-202] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [71-247] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [250-278] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-81] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [86-111] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-124] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [131-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-189] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-257] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-37] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-46] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-91] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-105] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-22] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-14] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-131] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-70] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-129] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-64] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-205] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-253] for track '28' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-295] for track '30' has 2 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.