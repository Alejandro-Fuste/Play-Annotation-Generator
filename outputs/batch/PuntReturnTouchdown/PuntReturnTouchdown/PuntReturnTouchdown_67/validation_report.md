# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_67`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 56 |
| Player Tracks | 56 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 262 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 135: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - Row 136: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [50-236] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [238-278] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-296] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-548] for track '1' has 10 frames without a visible bounding box.
> - Action 'Action_None' range [553-558] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-565] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-81] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-80] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-327] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-366] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-80] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-208] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-322] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-356] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-437] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-452] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-286] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-368] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [370-388] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-395] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-569] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-92] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-280] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [283-314] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-323] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-401] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-430] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [50-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-294] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-225] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-257] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-386] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-466] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-81] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [90-170] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-325] for track '16' has 9 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-105] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-63] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-39] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [50-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-77] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-170] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-189] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [274-366] for track '20' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [369-486] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [488-494] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-499] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-104] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-187] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-113] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-197] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [121-161] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-262] for track '26' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [122-135] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-206] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-237] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '30' starts at frame 241, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [241-241] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [244-296] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [301-302] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [310-314] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [319-322] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [324-328] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [330-346] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [350-420] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [422-551] for track '30' has 7 frames without a visible bounding box.
> - Action 'Action_CrossGoalLine' range [565-568] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-282] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-465] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-206] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-261] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-333] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [342-344] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-348] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-355] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-370] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-217] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-333] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [335-345] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-362] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-365] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-396] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-407] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-413] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-423] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-432] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [434-435] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-450] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [453-513] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-521] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-232] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-325] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-350] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-569] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [226-299] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-305] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-406] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-416] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [419-424] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-431] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-451] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-463] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-469] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-332] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-295] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-300] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-332] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-363] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [370-381] for track '39' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [385-386] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-390] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-296] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-335] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [337-368] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [371-497] for track '40' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [499-502] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-519] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-535] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [538-543] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-546] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-559] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-565] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-344] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-374] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-462] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-472] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-477] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-526] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-531] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-511] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [293-448] for track '44' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [450-485] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-305] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-343] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-356] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-521] for track '45' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [529-548] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [550-555] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-558] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-565] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-428] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-335] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-377] for track '49' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [372-417] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-422] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-426] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-466] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-485] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-497] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-393] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-569] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [414-415] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-425] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [428-455] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [457-460] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-470] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-490] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-486] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-491] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-499] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [502-505] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-531] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-537] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-540] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-548] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [530-531] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-536] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-539] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-563] for track '55' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.