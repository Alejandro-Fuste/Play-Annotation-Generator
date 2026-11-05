# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_66`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 58 |
| Player Tracks | 58 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 281 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 659 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 134: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - Row 134: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [93-179] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-191] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-214] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-394] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-400] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-406] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-416] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-207] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-272] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-502] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [512-515] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-618] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [622-623] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [630-640] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-104] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-346] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-383] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-419] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-432] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-515] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-522] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [524-543] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-554] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-567] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [572-575] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-601] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-614] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [625-628] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [651-653] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-54] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-273] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-374] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-485] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-165] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-243] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-297] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-445] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-625] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-471] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-191] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-384] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-27] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-173] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-251] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-265] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-370] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-381] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-443] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-530] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-160] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-230] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-226] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-320] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-148] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-280] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-289] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-56] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-240] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-348] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-330] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [347-385] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-398] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-462] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-485] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [504-515] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-558] for track '19' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [560-620] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [622-624] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-649] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [84-161] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-118] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-171] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-226] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-250] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-286] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [292-347] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [349-352] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [360-400] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [402-420] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [423-471] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-212] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-142] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-290] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [303-321] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-488] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-493] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-659] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-159] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-312] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-346] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-357] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [360-385] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [389-430] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-525] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [527-530] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-285] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-243] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-522] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [524-536] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [541-542] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-561] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [579-585] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [588-611] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-268] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-284] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-372] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-330] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-454] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [457-638] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-319] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-396] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-429] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-365] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-387] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [389-491] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-506] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-427] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-374] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-385] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-478] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [483-490] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [508-551] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [554-558] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-582] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-659] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [391-393] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-445] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [449-516] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [518-530] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-659] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-411] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-431] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-474] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-484] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-505] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [507-545] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [547-587] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [590-659] for track '40' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [446-538] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [541-543] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [546-594] for track '41' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [596-642] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_CrossGoalLine' range [643-644] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-476] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-521] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [524-527] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-591] for track '42' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [475-659] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-520] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-529] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [533-542] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [544-553] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [530-536] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [541-546] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-550] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-556] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-565] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-535] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-544] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [546-547] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-603] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [607-659] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-535] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-547] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-553] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [553-562] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [564-567] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [580-581] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-564] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [572-573] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [598-600] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [610-615] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [638-642] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [638-641] for track '56' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.