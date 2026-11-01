# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_131`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_131/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 174 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Segment 'Action_BlockSecondLevel' for track '11' has invalid range: start=200, end=169. Clamping end to start.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [155–168], lower_priority='Action_ZoneBlock' annotated_start=158, effective_Action_ZoneBlock_start=169.
> - Segment 'Action_ZoneBlock' for track '20' has invalid range: start=158, end=21. Clamping end to start.
> - Action 'Action_None' range [155-378] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-389] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-262] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-270] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-313] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-267] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-31] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-199] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-267] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-287] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-304] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-284] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-309] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-243] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-308] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [175-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '11' starts at frame 169, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [169-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-97] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-195] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-23] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-389] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-41] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-103] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-169] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-103] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-189] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-261] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-307] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-331] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [337-343] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-358] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-377] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-387] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [177-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [177-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [200-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-389] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-32] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-41] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-46] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-181] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-261] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-389] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-5] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-21] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-116] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [186-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [271-274] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [278-331] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-204] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-216] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-250] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-289] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-309] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-328] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [331-389] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-218] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-235] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-255] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-242] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-293] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-389] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-303] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-316] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [321-332] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [335-341] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-306] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-317] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-323] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-333] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-376] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-387] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-291] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-305] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-359] for track '32' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [361-389] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-331] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-331] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-384] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-325] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-332] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-329] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-389] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-341] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-351] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-372] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-387] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-373] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-389] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-357] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-366] for track '41' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.