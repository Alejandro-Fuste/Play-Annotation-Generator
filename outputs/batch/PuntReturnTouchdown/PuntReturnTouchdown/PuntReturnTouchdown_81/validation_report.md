# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_81`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_81/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 92 |
| Player Tracks | 92 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 335 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_CrossGoalLine' for track '7' has invalid range: start=593, end=152. Clamping end to start.
> - Action 'Action_None' range [64-172] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-220] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-110] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-343] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-110] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-247] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-243] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-86] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-253] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-273] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [275-282] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-141] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-148] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-235] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-245] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-345] for track '15' has 9 frames without a visible bounding box.
> - Action 'Action_None' range [347-364] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-376] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-560] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [562-586] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [591-594] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-114] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-80] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-110] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-202] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-233] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-247] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-275] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [278-282] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-315] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-75] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-176] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-310] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [313-392] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-395] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-409] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-418] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-220] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-250] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-287] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-317] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-333] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [337-398] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-154] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [157-170] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-243] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-267] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [269-327] for track '25' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-154] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-172] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-257] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-423] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [438-442] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-449] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-187] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-294] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-344] for track '30' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [346-360] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-449] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [479-590] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-596] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-280] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-310] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-378] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-233] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-247] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-266] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-282] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-294] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-304] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-317] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-353] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-220] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-241] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-225] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-268] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-282] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [291-382] for track '38' has 5 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [396-401] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-407] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-515] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [520-599] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-426] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-449] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-452] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-462] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-481] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-554] for track '40' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [557-558] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-255] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-282] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-308] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-316] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-330] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-381] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-301] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-315] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-366] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-268] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-283] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-322] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-350] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-392] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-316] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-322] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-335] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-380] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-392] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-409] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-367] for track '57' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [370-379] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-412] for track '57' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [332-344] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-356] for track '58' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [358-367] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-378] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-449] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-338] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-364] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-353] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-379] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-386] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-381] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-578] for track '62' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [580-584] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [592-598] for track '62' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [362-421] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [425-494] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [499-502] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-391] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-406] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-481] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-489] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-495] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-554] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-562] for track '64' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-376] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-416] for track '65' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [371-404] for track '66' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-418] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-449] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-453] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-599] for track '66' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-378] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-416] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-449] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-455] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-443] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-595] for track '69' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [406-407] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-419] for track '70' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [412-413] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-422] for track '71' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [435-448] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-421] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-489] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-419] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-442] for track '74' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [458-459] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-464] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-449] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-465] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-481] for track '75' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [494-506] for track '75' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [509-555] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-566] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-449] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-572] for track '77' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [574-582] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-590] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [595-599] for track '77' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-448] for track '78' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [496-526] for track '78' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [533-583] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [587-593] for track '78' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [453-466] for track '79' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [473-477] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-483] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-476] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-554] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-561] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-559] for track '83' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [565-566] for track '83' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [498-599] for track '84' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [499-554] for track '85' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-577] for track '85' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [586-599] for track '85' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-516] for track '86' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [507-510] for track '87' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-527] for track '88' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [530-561] for track '88' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [569-588] for track '88' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-567] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-575] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-582] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [587-588] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-598] for track '89' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [546-557] for track '90' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [559-563] for track '90' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [566-571] for track '90' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [567-575] for track '91' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '91' has undefined position. Will map to Position_Unknown.
> - Player track '91' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.