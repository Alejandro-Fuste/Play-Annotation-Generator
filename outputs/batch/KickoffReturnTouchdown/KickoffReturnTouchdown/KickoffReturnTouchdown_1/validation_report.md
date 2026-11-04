# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `KickoffReturnTouchdown_1`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 97 |
| Player Tracks | 97 |
| Ball Tracks | 0 |
| CSV events parsed | 5 |
| Action Segments inferred | 332 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Segment 'Action_KickBall' for track '11' has invalid range: start=69, end=56. Clamping end to start.
> - Segment 'Action_CrossGoalLine' for track '37' has invalid range: start=587, end=315. Clamping end to start.
> - Action 'Action_None' range [3-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-272] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-280] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-376] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-411] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-445] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-457] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [484-488] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-492] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-497] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-503] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [521-531] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-243] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-111] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-198] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-237] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-282] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-297] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-321] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-270] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-282] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-303] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-252] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-317] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-360] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-374] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-258] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-280] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-290] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-296] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-72] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-75] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-12] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-106] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-190] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [29-30] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [51-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [55-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-154] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-313] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-335] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-85] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-119] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-232] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-279] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-313] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-351] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-224] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-231] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-283] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-270] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-308] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-400] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [407-598] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [116-203] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-127] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-168] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-285] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-294] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-364] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-157] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-175] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-192] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-195] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-161] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-283] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-322] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [365-599] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-182] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-204] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-222] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-236] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-310] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [315-371] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-590] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_CatchKick' for track '37' starts at frame 187, but the player has no visible bounding box on this frame.
> - Action 'Action_CatchKick' range [187-190] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_CatchKick' range [202-209] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [210-286] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [314-315] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-208] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-233] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-599] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-203] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-221] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-243] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-290] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-371] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-378] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-383] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-386] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-397] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-411] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-432] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [434-437] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [453-477] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-587] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-255] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-378] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-397] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-415] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-438] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [444-445] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-464] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-470] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-478] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-489] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-499] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-509] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [511-528] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [532-533] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-537] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-545] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-564] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-326] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-361] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-271] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-249] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-282] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-299] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-388] for track '46' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [395-452] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-457] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-464] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-483] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-332] for track '47' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [264-277] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-299] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-310] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-386] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-397] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-473] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-478] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-509] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-539] for track '48' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [280-289] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-296] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-345] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-361] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [431-599] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-314] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-428] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-432] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-440] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-452] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-540] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-599] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-297] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-333] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-337] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-358] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-314] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-331] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-400] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-411] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-426] for track '53' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [315-353] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [360-362] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-369] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-351] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-359] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-386] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [391-397] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-405] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-422] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-428] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-432] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-440] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-450] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-461] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [484-502] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-370] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-422] for track '58' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [379-452] for track '59' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [454-457] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-599] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-442] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [445-475] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [478-480] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-484] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-506] for track '60' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [508-557] for track '60' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [559-571] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [574-575] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-387] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-392] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-396] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-450] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-569] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [571-572] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-397] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-479] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [485-557] for track '65' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [565-566] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [572-579] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-422] for track '66' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [412-416] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-424] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-429] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-446] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-462] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-478] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-496] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-438] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-432] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-573] for track '72' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [447-452] for track '73' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [463-464] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-475] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-470] for track '74' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [480-494] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-522] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-550] for track '74' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [463-464] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-543] for track '76' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [553-554] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-563] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-567] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-583] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-475] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-599] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-533] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-542] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-495] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [498-599] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-506] for track '82' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-509] for track '83' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-568] for track '83' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [508-517] for track '84' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-541] for track '84' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [544-553] for track '84' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [511-514] for track '85' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-520] for track '86' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-533] for track '87' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-557] for track '88' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-563] for track '88' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [571-572] for track '89' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [576-578] for track '90' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [587-590] for track '90' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-585] for track '91' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [587-599] for track '92' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [596-599] for track '95' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.