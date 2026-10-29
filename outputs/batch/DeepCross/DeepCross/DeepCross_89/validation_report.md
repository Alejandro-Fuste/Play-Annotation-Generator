# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_89`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 209 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 92: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 92: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 92: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 92: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_BallCarry' range [163-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [271-275] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [277-278] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [282-283] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [285-286] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [290-316] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [323-339] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [347-348] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-129] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-124] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [129-241] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [243-279] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-309] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [312-341] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-349] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-367] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-379] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-183] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-233] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-33] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-264] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [267-275] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [279-280] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [290-295] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-232] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-252] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-266] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-341] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-358] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-57] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-200] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-272] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-104] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-146] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-145] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-221] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-238] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-261] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-280] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-328] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-376] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-114] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-160] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-330] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-339] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-345] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-111] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-26] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-245] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-265] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-354] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-48] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [186-228] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [238-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [247-287] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [289-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [301-311] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [314-318] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [320-331] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [337-338] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [341-345] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [366-368] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [371-373] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [377-378] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-228] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-247] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-389] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-51] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-71] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-278] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-339] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-90] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-117] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-220] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-289] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-356] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-142] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-228] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-240] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-264] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-282] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-300] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [303-305] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-293] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-309] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-296] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-312] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-341] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-351] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-361] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-386] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-310] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [305-308] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-320] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-314] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-334] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-348] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-360] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-375] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-382] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-350] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-358] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-369] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-363] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-361] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-368] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-377] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '50' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.