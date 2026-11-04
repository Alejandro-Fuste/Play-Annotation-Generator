# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_73`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_73/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 176 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Segment 'Action_CatchKick' for track '25' has invalid range: start=215, end=211. Clamping end to start.
> - Action 'Action_None' range [40-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-274] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-282] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-297] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-312] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-321] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-406] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-440] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-222] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-261] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-412] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [415-419] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-424] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-430] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-434] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-569] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-221] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-272] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-281] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-303] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-323] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [325-362] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-252] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-262] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-322] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-348] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-416] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-233] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-286] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-411] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-282] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-303] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-312] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-413] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [40-92] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-186] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-196] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-399] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [401-423] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-427] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-434] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-302] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-417] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-266] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-281] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-303] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-354] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [356-391] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [393-410] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 40, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [40-40] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-62] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [64-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-93] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-236] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-266] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-378] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-283] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-249] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [256-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-282] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-313] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-569] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-58] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-186] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-204] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-232] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-118] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-151] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-189] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-140] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-217] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-255] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-184] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [186-195] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-282] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-312] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-414] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-442] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-224] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-267] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-303] for track '23' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [305-369] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-212] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-345] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-352] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-371] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-559] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-303] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-312] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-359] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-304] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-311] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-430] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-345] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-383] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [393-396] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-460] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-466] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-480] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-496] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [554-555] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-569] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-558] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-569] for track '39' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.