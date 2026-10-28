# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_25`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 158 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [53–70], lower_priority='Action_PassBlock' annotated_start=56, effective_Action_PassBlock_start=71.
> - Action 'Action_None' range [53-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-173] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-185] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-283] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-295] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-355] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-133] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-150] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-218] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-408] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-335] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-349] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-369] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-291] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-337] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-355] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [358-361] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-370] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [150-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-178] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-285] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [53-304] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-310] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-344] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-395] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-449] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-449] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-291] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-359] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-142] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [85-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-297] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-344] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-76] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-268] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-315] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-185] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [190-327] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-335] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-186] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-369] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-204] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-333] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-207] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-329] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-346] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-373] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-252] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-205] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-254] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-274] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-291] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-406] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-234] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-283] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-290] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-449] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-362] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-265] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-293] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-300] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-315] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-449] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-318] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-349] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-360] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-367] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-290] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-314] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-327] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-340] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-350] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-359] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-371] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '44' has 1 frames without a visible bounding box.
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
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.