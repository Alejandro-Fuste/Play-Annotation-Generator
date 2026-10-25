# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_83`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 145: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 146: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [28–44], lower_priority='Action_RunBlock' annotated_start=38, effective_Action_RunBlock_start=45.
> - Action 'Action_None' range [28-299] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-269] for track '1' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [28-262] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-234] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-161] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-266] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-194] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-85] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [38-60] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [71-78] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [83-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [159-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [180-229] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [231-237] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [240-250] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [51-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-263] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-270] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-290] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-229] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-278] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [38-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [59-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [45-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [38-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [38-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [201-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [248-256] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-265] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-123] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-196] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-236] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-255] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-273] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-288] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-296] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-197] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [200-254] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-195] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [197-212] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-253] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-293] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-242] for track '30' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-264] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-289] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-245] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '36' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.