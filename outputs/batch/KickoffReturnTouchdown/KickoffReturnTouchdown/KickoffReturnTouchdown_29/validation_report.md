# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_29`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 108 |
| Player Tracks | 108 |
| Ball Tracks | 0 |
| CSV events parsed | 8 |
| Action Segments inferred | 448 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Segment 'Action_KickApproach' for track '9' has invalid range: start=27, end=9. Clamping end to start.
> - Segment 'Action_KickBall' for track '9' has invalid range: start=85, end=9. Clamping end to start.
> - Segment 'Action_CatchKick' for track '51' has invalid range: start=235, end=201. Clamping end to start.
> - Action 'Action_None' range [27-170] for track '0' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [185-200] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [208-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-238] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-135] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-220] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-161] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-105] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-246] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [249-289] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-407] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-420] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [422-428] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [439-446] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-109] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-161] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-66] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-53] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-9] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-54] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-71] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-253] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-310] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-398] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-420] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-517] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [521-522] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-534] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-547] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [553-554] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-564] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-177] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-217] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-234] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-260] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-260] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-113] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [116-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-126] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-134] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-154] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-398] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [400-402] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-413] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-423] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-126] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-224] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-396] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-400] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-413] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-425] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [435-470] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [473-476] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-497] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [502-503] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-510] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-513] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-569] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-138] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-144] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-167] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-198] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-569] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-172] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-159] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-200] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-179] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-193] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-212] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-238] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-184] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-198] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-199] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-189] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-197] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-219] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-323] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-332] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-224] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-287] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-418] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-465] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-471] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-481] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [483-511] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-229] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-310] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-364] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-222] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-332] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [343-354] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [357-365] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-388] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-225] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-240] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-241] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-418] for track '48' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [420-425] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-433] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-444] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-452] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-487] for track '48' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [490-497] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-503] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-245] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-270] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-287] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-420] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [422-463] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [465-515] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [520-526] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [528-532] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-240] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-326] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-257] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [260-264] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [266-267] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [272-284] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [296-297] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [310-337] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [339-340] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [343-357] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [359-362] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [365-385] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [387-391] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [398-400] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [402-406] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [409-411] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [413-416] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [423-448] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [456-472] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [474-482] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [508-510] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [515-527] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [529-555] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_CrossGoalLine' range [556-569] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-280] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-357] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [360-383] for track '52' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-396] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-413] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-438] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-473] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-490] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [502-514] for track '52' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-286] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-296] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-311] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-369] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-381] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-387] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-288] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-303] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-344] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-357] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-402] for track '54' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [404-413] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [416-420] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-439] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [441-442] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-448] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-456] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-460] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-357] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-394] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-400] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-435] for track '55' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [437-438] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-453] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-463] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-475] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-511] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-404] for track '56' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [409-414] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [416-426] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-435] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-448] for track '56' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [451-463] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [465-470] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-492] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-297] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-296] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-309] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-374] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-390] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-486] for track '59' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [491-492] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-554] for track '59' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-321] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-332] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-414] for track '60' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [420-422] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-433] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-407] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-413] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-420] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-428] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-476] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-486] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [489-490] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-496] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-501] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-510] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-520] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-367] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-382] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-396] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-403] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-414] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-428] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-473] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-504] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [506-507] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-541] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-556] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-569] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-350] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-369] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-365] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-377] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-388] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-414] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-418] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-425] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-459] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-396] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-400] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-400] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-400] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-413] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-437] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-446] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-414] for track '71' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [401-409] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-418] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-426] for track '72' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [429-435] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-439] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-446] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-463] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-468] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-482] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-498] for track '72' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-418] for track '73' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [452-453] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-458] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-478] for track '73' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-490] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-497] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-501] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-515] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-529] for track '73' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [536-539] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-549] for track '73' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [553-554] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-567] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-420] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-425] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-435] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-420] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-428] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-446] for track '75' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [448-449] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-457] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-439] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-470] for track '76' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [473-504] for track '76' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [506-508] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-521] for track '76' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [523-525] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-532] for track '76' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [534-539] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-542] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-420] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-463] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-467] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-425] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-425] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-441] for track '79' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [446-461] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-486] for track '79' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [489-494] for track '79' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [498-507] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-429] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-428] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-465] for track '82' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [480-484] for track '82' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [490-491] for track '82' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-500] for track '82' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-437] for track '83' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '84' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-450] for track '85' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-494] for track '85' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [496-501] for track '85' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [452-458] for track '86' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-491] for track '86' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-518] for track '86' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [532-545] for track '86' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [456-457] for track '87' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-460] for track '88' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-470] for track '88' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-475] for track '88' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-477] for track '89' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [480-488] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-499] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [502-508] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-528] for track '89' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [532-565] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-463] for track '90' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-467] for track '90' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-465] for track '91' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-468] for track '92' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-478] for track '93' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-486] for track '93' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [489-496] for track '93' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [499-507] for track '93' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-569] for track '93' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '94' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-480] for track '95' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-496] for track '96' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [502-504] for track '96' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-511] for track '96' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-525] for track '96' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-530] for track '96' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-569] for track '96' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-480] for track '97' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-484] for track '98' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-500] for track '98' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [504-509] for track '98' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [514-515] for track '98' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-537] for track '98' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-501] for track '99' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-506] for track '99' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [547-559] for track '99' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-519] for track '100' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-523] for track '101' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-553] for track '102' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-565] for track '102' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-569] for track '102' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-540] for track '103' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-540] for track '104' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-543] for track '105' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-569] for track '106' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '107' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '92' has undefined position. Will map to Position_Unknown.
> - Player track '92' has undefined team_side. Will map to Team_Unknown.
> - Player track '93' has undefined position. Will map to Position_Unknown.
> - Player track '93' has undefined team_side. Will map to Team_Unknown.
> - Player track '94' has undefined position. Will map to Position_Unknown.
> - Player track '94' has undefined team_side. Will map to Team_Unknown.
> - Player track '95' has undefined position. Will map to Position_Unknown.
> - Player track '95' has undefined team_side. Will map to Team_Unknown.
> - Player track '96' has undefined position. Will map to Position_Unknown.
> - Player track '96' has undefined team_side. Will map to Team_Unknown.
> - Player track '97' has undefined position. Will map to Position_Unknown.
> - Player track '97' has undefined team_side. Will map to Team_Unknown.
> - Player track '98' has undefined position. Will map to Position_Unknown.
> - Player track '98' has undefined team_side. Will map to Team_Unknown.
> - Player track '99' has undefined position. Will map to Position_Unknown.
> - Player track '99' has undefined team_side. Will map to Team_Unknown.
> - Player track '100' has undefined position. Will map to Position_Unknown.
> - Player track '100' has undefined team_side. Will map to Team_Unknown.
> - Player track '101' has undefined position. Will map to Position_Unknown.
> - Player track '101' has undefined team_side. Will map to Team_Unknown.
> - Player track '102' has undefined position. Will map to Position_Unknown.
> - Player track '102' has undefined team_side. Will map to Team_Unknown.
> - Player track '103' has undefined position. Will map to Position_Unknown.
> - Player track '103' has undefined team_side. Will map to Team_Unknown.
> - Player track '104' has undefined position. Will map to Position_Unknown.
> - Player track '104' has undefined team_side. Will map to Team_Unknown.
> - Player track '105' has undefined position. Will map to Position_Unknown.
> - Player track '105' has undefined team_side. Will map to Team_Unknown.
> - Player track '106' has undefined position. Will map to Position_Unknown.
> - Player track '106' has undefined team_side. Will map to Team_Unknown.
> - Player track '107' has undefined position. Will map to Position_Unknown.
> - Player track '107' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.