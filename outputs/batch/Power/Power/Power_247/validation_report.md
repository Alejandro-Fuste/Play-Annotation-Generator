# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_247`
- **Input XML**: `outputs/batch/Power/Power/Power_247/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 496: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PreSnap' range [15-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-258] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-301] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-395] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-449] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-275] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-278] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-330] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-334] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-434] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [442-444] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [447-449] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-287] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-304] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-318] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-414] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [425-434] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-257] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-274] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-325] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-411] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-444] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-279] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-436] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-333] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-346] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-312] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [253-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [265-266] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [268-274] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-352] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-449] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-422] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-289] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-295] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-307] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-400] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-413] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-250] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-330] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-336] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-292] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-280] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-300] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-306] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-316] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-320] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-330] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-364] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-326] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-354] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-334] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-367] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-355] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-390] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-402] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [438-439] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-404] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-413] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [429-431] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [433-446] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-401] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-404] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [421-423] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [426-429] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [432-437] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [440-449] for track '37' has 2 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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