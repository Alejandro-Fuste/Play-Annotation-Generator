# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_149`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_149/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 272: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-235] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-234] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-182] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-174] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-194] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-219] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-236] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-257] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-273] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-289] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-102] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-264] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-270] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-293] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-297] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [82-249] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [252-265] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [270-271] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-202] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-129] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-242] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-261] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-289] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-196] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-216] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-193] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-195] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-237] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-220] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-228] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-268] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-279] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-289] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-217] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-226] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-262] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-237] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-242] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-243] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-263] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-283] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-286] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-252] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-264] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-274] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-283] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-297] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-273] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-279] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-299] for track '42' has 1 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.