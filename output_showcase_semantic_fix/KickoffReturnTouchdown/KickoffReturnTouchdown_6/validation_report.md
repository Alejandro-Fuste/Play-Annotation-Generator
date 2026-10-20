# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_6`
- **Input XML**: `output_showcase_semantic_fix/KickoffReturnTouchdown/KickoffReturnTouchdown_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 57 |
| Player Tracks | 56 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 259 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 689 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
> - Segment 'Action_CatchKick' for track '33' has invalid range: start=278, end=253. Clamping end to start.
> - Segment 'Action_CrossGoalLine' for track '33' has invalid range: start=687, end=589. Clamping end to start.
> - Action 'Action_None' range [72-133] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-247] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-264] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-287] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-307] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-176] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-290] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-354] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-363] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-453] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [456-479] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [482-488] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-667] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [670-671] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-181] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-193] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-284] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-300] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-339] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-181] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-198] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-265] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-289] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-368] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-181] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-207] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-249] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-290] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [292-329] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [333-371] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-382] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-408] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-248] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-262] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-333] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [336-354] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-372] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-396] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-248] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-282] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [284-296] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-326] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-345] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-372] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-385] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-417] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-239] for track '9' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [244-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-421] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [72-110] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [119-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-242] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-341] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-461] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [72-251] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-353] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-326] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [329-375] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-205] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-266] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-279] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-295] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-380] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-417] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-425] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-179] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-195] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-248] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-285] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-337] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [380-391] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [402-407] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-418] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-421] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-457] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [459-643] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [654-658] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-195] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-258] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-49] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-96] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-214] for track '17' has 9 frames without a visible bounding box.
> - Action 'Action_None' range [216-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-304] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-343] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-408] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-416] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-436] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [438-439] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-164] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-182] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-224] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-86] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-201] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-217] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-246] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-263] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-293] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-326] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-345] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-384] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-465] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [468-596] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-338] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [344-348] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-206] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-269] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-254] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-266] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-336] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-415] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-373] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-385] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-397] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [286-287] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [289-294] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [296-298] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [303-584] for track '33' has 7 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [588-589] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-349] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-416] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-429] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-324] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-355] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [361-603] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [605-606] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [608-610] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [614-618] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-627] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-377] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-394] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-401] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-409] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-386] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-400] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-689] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [356-365] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-384] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-421] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [383-401] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-399] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-464] for track '42' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [468-604] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [608-609] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [614-616] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [618-619] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-492] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-663] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [484-486] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-551] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-497] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-629] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [633-665] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-689] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-604] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-622] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-581] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-620] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-592] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [607-609] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [616-638] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [640-641] for track '55' has 1 frames without a visible bounding box.
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
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.