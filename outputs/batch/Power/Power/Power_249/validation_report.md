# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_249`
- **Input XML**: `outputs/batch/Power/Power/Power_249/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 118 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 499: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 499: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [16-303] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-347] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-316] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-335] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-389] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-336] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-349] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-352] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-366] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-376] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-234] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-255] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-372] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-389] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-208] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-368] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-248] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-297] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [179-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [231-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-281] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [285-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-307] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-313] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-317] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-325] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-330] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-334] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-345] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-377] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-389] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-325] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-274] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-291] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-301] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-308] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-351] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-357] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-247] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [179-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-389] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-254] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-258] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-389] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-301] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-340] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-227] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-233] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-252] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-24] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-36] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-306] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-317] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-327] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-348] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-365] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-374] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-386] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-261] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-322] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-389] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-290] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-324] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-366] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-389] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-291] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-292] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-312] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-320] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-344] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-348] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-319] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-336] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-365] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-372] for track '36' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.