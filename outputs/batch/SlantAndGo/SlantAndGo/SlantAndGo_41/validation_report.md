# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_41`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 55: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 56: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 56: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [31–46], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=47.
> - Action 'Action_None' range [31-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-168] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-186] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-202] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [204-212] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-184] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-220] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [31-199] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-219] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-287] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-216] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-276] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-196] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-220] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [31-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-250] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-259] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-268] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-98] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [101-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-302] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-329] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-303] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [136-140] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [142-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [99-271] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [273-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-235] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-327] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-105] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [152-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-77] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-96] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-216] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-211] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-205] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-221] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-221] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-217] for track '32' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [219-223] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-235] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-219] for track '33' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.