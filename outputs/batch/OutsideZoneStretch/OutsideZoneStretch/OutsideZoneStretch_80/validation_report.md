# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_80`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 136 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '15' has invalid range: start=223, end=219. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '16' has invalid range: start=223, end=203. Clamping end to start.
> - Action 'Action_PreSnap' range [0-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-306] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-302] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-312] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-47] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-213] for track '2' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-282] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-416] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-449] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-197] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-211] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-225] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-232] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-295] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-449] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-449] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-403] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [411-415] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-366] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-219] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-211] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-245] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-256] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-370] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-449] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-306] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-350] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [230-258] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-336] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-449] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-449] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-197] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-211] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-449] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-200] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [223-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [227-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [239-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [245-247] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-219] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [247-258] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [270-282] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [285-288] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-346] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [351-424] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-200] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [227-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-266] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-303] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-27] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-35] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-57] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-199] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-213] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-355] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-379] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-259] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-265] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-288] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-306] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-395] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-300] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-289] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-382] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-306] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-341] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-428] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [431-439] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [442-447] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-449] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-338] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-330] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-330] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-346] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-350] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-358] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-362] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-355] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-379] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-409] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-359] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-392] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-406] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [437-440] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [442-446] for track '38' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.