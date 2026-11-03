# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_27`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 54 |
| Player Tracks | 54 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 174 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 30: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [27–42], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=43.
> - Action 'Action_RunPostRoute' range [42-303] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [305-328] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [331-363] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [367-390] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [392-393] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-365] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [370-376] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-243] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-419] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-419] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-276] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-277] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-287] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-380] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [386-393] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-408] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-413] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-197] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-215] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-273] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-345] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-370] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-415] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-326] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-253] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-273] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-313] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-288] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-322] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-340] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-324] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-392] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-417] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-207] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-237] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-318] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-419] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-338] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-330] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-349] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-320] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [322-393] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-314] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-389] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [94-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [101-259] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [261-419] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-328] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [332-367] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [370-371] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-57] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [144-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-278] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-244] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-212] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-244] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-250] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-322] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-323] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-351] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-359] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-343] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-363] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-387] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-401] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-410] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-345] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-386] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-419] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-390] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-400] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-410] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-390] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-402] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-408] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-412] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-415] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-417] for track '53' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.