# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_5`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 136 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 12: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 98 frames exceeds threshold 90 frames [start=174, end=271].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 98 frames exceeds threshold 90 frames [start=174, end=271].
> - Action 'Action_None' range [171-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-293] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-240] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-414] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-230] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-278] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-383] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-399] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [405-412] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-432] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-441] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-256] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-278] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [282-285] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-234] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-191] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-393] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-357] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-390] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-398] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [401-408] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-420] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [423-427] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-437] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [439-449] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-201] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-373] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [377-381] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-405] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-410] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-390] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-443] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [171-253] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-195] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [197-214] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-238] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-243] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-449] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-250] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-253] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-393] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-449] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-392] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-446] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-352] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-362] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-367] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-370] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-393] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-404] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-411] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-416] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-429] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-441] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-364] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-382] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-375] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-404] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-421] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-411] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-431] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-437] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-449] for track '38' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.