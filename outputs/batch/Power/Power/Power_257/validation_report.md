# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_257`
- **Input XML**: `outputs/batch/Power/Power/Power_257/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 154 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 514: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
> - Row 514: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [11-363] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-380] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-286] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-302] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-419] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-307] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-395] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-246] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-273] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-294] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-313] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-322] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-340] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-348] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-360] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-366] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-370] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-384] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-418] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-238] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-380] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-253] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-354] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-358] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-361] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-366] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-376] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-384] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-390] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-396] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-406] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-412] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-214] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-221] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-245] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-245] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-266] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-325] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-328] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-333] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-340] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [198-201] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [214-215] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-368] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-419] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [186-218] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-34] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-183] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-214] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-222] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-237] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-246] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-266] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-109] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-218] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-31] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-49] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-189] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [204-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-269] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-414] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [416-417] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-330] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-397] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-248] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-419] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-262] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-377] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-406] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-328] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-278] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-363] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-369] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-409] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-419] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-322] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-329] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-334] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-329] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-396] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-401] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-406] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-410] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-416] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-327] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-347] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-366] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-376] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-395] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-406] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-410] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [413-418] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-324] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-362] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-369] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [371-375] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-384] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-396] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-401] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-410] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-419] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-319] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-358] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-413] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-384] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-419] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-369] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-381] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-396] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-370] for track '44' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.