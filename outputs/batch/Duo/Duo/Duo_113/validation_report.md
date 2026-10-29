# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_113`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_113/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 221 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 568 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 568 as fallback play end.
> - Overlapping action conflict at frame 136 for track '3': 'Action_ComboBlock' vs 'Action_BlockSecondLevel'. Overriding with 'Action_BlockSecondLevel'.
> - Action 'Action_PreSnap' range [0-497] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [502-539] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [544-545] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [547-568] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-295] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-303] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-311] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-429] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [432-433] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [436-437] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [440-441] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [452-453] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [456-458] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [460-461] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [470-474] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-490] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [495-496] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [498-500] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [503-506] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-539] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [548-556] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-482] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-527] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-490] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-117] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-211] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-279] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-421] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [424-426] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [432-433] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [449-466] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [474-518] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-568] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-504] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-517] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-211] for track '11' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-522] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [524-525] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [527-558] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [562-563] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-121] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-130] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-211] for track '12' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-279] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-474] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [477-496] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [499-541] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [544-546] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [552-553] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-114] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-437] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [440-441] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [444-481] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [528-538] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [548-549] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [551-557] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [562-568] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-41] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-117] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-207] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-275] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-291] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-295] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-303] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-311] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-433] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [436-437] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [440-441] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [444-445] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [448-521] for track '14' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [524-525] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [528-533] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [536-537] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [540-541] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [544-545] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [552-553] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-45] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-71] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-279] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-538] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [544-554] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [556-563] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-46] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-105] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-114] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-211] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-275] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-295] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-303] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-311] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-316] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-429] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [432-433] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [450-568] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-513] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-457] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-21] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-211] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-228] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-21] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-117] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-151] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-207] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-279] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-295] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-303] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-453] for track '20' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [458-462] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [464-538] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [540-541] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-337] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-342] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-350] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-377] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-383] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-401] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [448-534] for track '22' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [536-537] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [544-546] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-442] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [444-447] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [449-463] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [466-474] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [497-521] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [528-530] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [532-568] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [479-498] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.