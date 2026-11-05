# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_86`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_86/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 91 |
| Player Tracks | 91 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 333 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 174: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_CrossGoalLine' for track '39' has invalid range: start=610, end=601. Clamping end to start.
> - Action 'Action_None' range [39-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-409] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-250] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-280] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-306] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [315-320] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-325] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-345] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-374] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-475] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-479] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-237] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-297] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-345] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-362] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-393] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [395-400] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [424-425] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-320] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [330-335] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-360] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-364] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-421] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [423-523] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-172] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-305] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-77] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-139] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-244] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-174] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-188] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-209] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-230] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-322] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-193] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [200-232] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-142] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-474] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [480-482] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-511] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [513-517] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-539] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [543-552] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-559] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-203] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-235] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-283] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-178] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' for track '19' starts at frame 39, but the player has no visible bounding box on this frame.
> - Action 'Action_LongSnap' range [39-46] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [51-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-250] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-261] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-392] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-410] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-83] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-101] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-133] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-193] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-206] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-249] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-231] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [241-242] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-260] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-277] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-325] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-332] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-193] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-212] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-219] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-376] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-380] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-377] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-388] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-402] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-412] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-419] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-348] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-352] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-370] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-411] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-467] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [469-585] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-601] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [603-619] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [621-629] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-285] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-300] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-332] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-339] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-347] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-366] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-373] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-377] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-384] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-394] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-332] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-591] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [595-601] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-307] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-317] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-395] for track '40' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-406] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-437] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-410] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-413] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-419] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-426] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-436] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-448] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-455] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-467] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-470] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-477] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-554] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [587-588] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-593] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-600] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-295] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-335] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-423] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-303] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-312] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-322] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-333] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-320] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-307] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-327] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-417] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-421] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-333] for track '48' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [339-343] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-337] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-618] for track '52' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-346] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-392] for track '53' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [394-495] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-366] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-370] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-377] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-389] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-460] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-475] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [481-483] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-508] for track '58' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [510-545] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-548] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-565] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-578] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-391] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-405] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-410] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-423] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-428] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-430] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-433] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-442] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-449] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-567] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [574-624] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-504] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-611] for track '64' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-461] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-483] for track '65' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [485-503] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-627] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [441-461] for track '66' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [463-476] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-488] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-455] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-459] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-473] for track '67' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [456-459] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-485] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-488] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-491] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-459] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-462] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-613] for track '70' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [486-489] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-537] for track '72' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [539-542] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-564] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-583] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-629] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-493] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-539] for track '74' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [542-557] for track '74' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [518-525] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-536] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-545] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-557] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-578] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-542] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-575] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-591] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-554] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-562] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-573] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-595] for track '79' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [597-598] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-606] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [608-615] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [618-619] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-629] for track '79' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [553-554] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-575] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [582-589] for track '82' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [592-596] for track '82' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [603-607] for track '82' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-595] for track '83' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-598] for track '84' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [621-623] for track '86' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [627-629] for track '86' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [622-623] for track '88' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [626-627] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-629] for track '90' has 1 frames without a visible bounding box.
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
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.
> - Player track '67' has undefined position. Will map to Position_Unknown.
> - Player track '67' has undefined team_side. Will map to Team_Unknown.
> - Player track '68' has undefined position. Will map to Position_Unknown.
> - Player track '68' has undefined team_side. Will map to Team_Unknown.
> - Player track '69' has undefined position. Will map to Position_Unknown.
> - Player track '69' has undefined team_side. Will map to Team_Unknown.
> - Player track '70' has undefined position. Will map to Position_Unknown.
> - Player track '70' has undefined team_side. Will map to Team_Unknown.
> - Player track '71' has undefined position. Will map to Position_Unknown.
> - Player track '71' has undefined team_side. Will map to Team_Unknown.
> - Player track '72' has undefined position. Will map to Position_Unknown.
> - Player track '72' has undefined team_side. Will map to Team_Unknown.
> - Player track '73' has undefined position. Will map to Position_Unknown.
> - Player track '73' has undefined team_side. Will map to Team_Unknown.
> - Player track '74' has undefined position. Will map to Position_Unknown.
> - Player track '74' has undefined team_side. Will map to Team_Unknown.
> - Player track '75' has undefined position. Will map to Position_Unknown.
> - Player track '75' has undefined team_side. Will map to Team_Unknown.
> - Player track '76' has undefined position. Will map to Position_Unknown.
> - Player track '76' has undefined team_side. Will map to Team_Unknown.
> - Player track '77' has undefined position. Will map to Position_Unknown.
> - Player track '77' has undefined team_side. Will map to Team_Unknown.
> - Player track '78' has undefined position. Will map to Position_Unknown.
> - Player track '78' has undefined team_side. Will map to Team_Unknown.
> - Player track '79' has undefined position. Will map to Position_Unknown.
> - Player track '79' has undefined team_side. Will map to Team_Unknown.
> - Player track '80' has undefined position. Will map to Position_Unknown.
> - Player track '80' has undefined team_side. Will map to Team_Unknown.
> - Player track '81' has undefined position. Will map to Position_Unknown.
> - Player track '81' has undefined team_side. Will map to Team_Unknown.
> - Player track '82' has undefined position. Will map to Position_Unknown.
> - Player track '82' has undefined team_side. Will map to Team_Unknown.
> - Player track '83' has undefined position. Will map to Position_Unknown.
> - Player track '83' has undefined team_side. Will map to Team_Unknown.
> - Player track '84' has undefined position. Will map to Position_Unknown.
> - Player track '84' has undefined team_side. Will map to Team_Unknown.
> - Player track '85' has undefined position. Will map to Position_Unknown.
> - Player track '85' has undefined team_side. Will map to Team_Unknown.
> - Player track '86' has undefined position. Will map to Position_Unknown.
> - Player track '86' has undefined team_side. Will map to Team_Unknown.
> - Player track '87' has undefined position. Will map to Position_Unknown.
> - Player track '87' has undefined team_side. Will map to Team_Unknown.
> - Player track '88' has undefined position. Will map to Position_Unknown.
> - Player track '88' has undefined team_side. Will map to Team_Unknown.
> - Player track '89' has undefined position. Will map to Position_Unknown.
> - Player track '89' has undefined team_side. Will map to Team_Unknown.
> - Player track '90' has undefined position. Will map to Position_Unknown.
> - Player track '90' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.