# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `KickoffReturnTouchdown_98`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_98/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 84 |
| Player Tracks | 84 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 281 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 100, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '636,642,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Segment 'Action_CatchKick' for track '31' has invalid range: start=235, end=198. Clamping end to start.
> - Action 'Action_None' range [18-358] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-226] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-243] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-288] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-224] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-287] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-153] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-184] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-251] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-283] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-296] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-315] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-364] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-375] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-401] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [405-489] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [497-502] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-512] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [514-521] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-629] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-239] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-450] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-201] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [214-334] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [412-629] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-215] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-62] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-263] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-245] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [18-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-131] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-275] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-290] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-305] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-331] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-56] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-13] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-215] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-241] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-231] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-264] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-377] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-130] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-231] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-249] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-125] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-243] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-151] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-230] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-249] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-261] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-267] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [316-317] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-300] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-251] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-256] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-519] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [523-542] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-553] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-629] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-440] for track '37' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [455-512] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-515] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-527] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-548] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-566] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-308] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-471] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [473-488] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-497] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-504] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-512] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-325] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [328-366] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-382] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-394] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-408] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-429] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [441-442] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-349] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-336] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-352] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-629] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-409] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [412-550] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-339] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-371] for track '46' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [376-502] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [554-577] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [589-600] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [605-606] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [610-615] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-393] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-416] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [420-497] for track '47' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [502-510] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [515-519] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-357] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-349] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-363] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-507] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-359] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-362] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-435] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-444] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-452] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-519] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-527] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-533] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-595] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-409] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-445] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [368-371] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-411] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-373] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-402] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-416] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-408] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [420-423] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-430] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-437] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-453] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-459] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-497] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-507] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [510-512] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-518] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-527] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-546] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-551] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-559] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-426] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [438-439] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-515] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-629] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-483] for track '62' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [413-623] for track '63' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [417-521] for track '64' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [524-629] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-428] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-438] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-457] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-532] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [535-544] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-562] for track '65' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [564-566] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-426] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-470] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-488] for track '66' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [432-438] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-471] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-476] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-481] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-495] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-508] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-462] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-508] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-512] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-521] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-578] for track '69' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [580-602] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [605-610] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [616-618] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [621-622] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-542] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-464] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-491] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-515] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-519] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-536] for track '73' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [547-571] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [576-578] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-610] for track '73' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [508-510] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-524] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-555] for track '75' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [557-567] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-629] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-520] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-536] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-550] for track '78' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [557-564] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-629] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-553] for track '79' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [555-571] for track '79' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [576-578] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-557] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-587] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [616-617] for track '83' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_98'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.