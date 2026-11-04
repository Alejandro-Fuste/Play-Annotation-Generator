# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_11`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 71 |
| Player Tracks | 71 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 215 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 24: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Segment 'Action_CrossGoalLine' for track '45' has invalid range: start=630, end=629. Clamping end to start.
> - Action 'Action_None' range [108-500] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [502-507] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-434] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [437-440] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [443-509] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [512-629] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-629] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-243] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [245-431] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [433-474] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-481] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [488-502] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-173] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-229] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-367] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-562] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-191] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-418] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-495] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-501] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-525] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [527-530] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-538] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [544-549] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-562] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [566-568] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-578] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [588-594] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-601] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-319] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-199] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-221] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-236] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-313] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-229] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-14] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-334] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-445] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-543] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-341] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [150-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [155-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-185] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-197] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-208] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-339] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-241] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-440] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-471] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-475] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-486] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [488-629] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-433] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-561] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [566-570] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-601] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-261] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-229] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-266] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-272] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-289] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [303-313] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-344] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-341] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-471] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-535] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [538-539] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-629] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-351] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-372] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-378] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-418] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-336] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-323] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-327] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-336] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-351] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-629] for track '43' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [274-357] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-372] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [302-629] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-301] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-347] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-429] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-333] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-352] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-537] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-474] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-477] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-536] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [544-562] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-565] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-570] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-374] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-380] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-389] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [391-393] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-400] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-404] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-409] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-427] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-473] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [476-506] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-512] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-519] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-526] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-396] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-597] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-382] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-397] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-411] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-542] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-407] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-431] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-485] for track '59' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [487-628] for track '59' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [412-413] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-505] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-595] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [597-599] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [605-621] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-534] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [497-501] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-524] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [526-539] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [542-559] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-573] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [576-604] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [606-614] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [616-619] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-553] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-565] for track '64' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [572-575] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-524] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-525] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-629] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-565] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-578] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-629] for track '68' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [598-604] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [609-611] for track '70' has 1 frames without a visible bounding box.
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
> - Action event 'Action_CrossGoalLine' has invalid start frame 630. Video range is [0, 629].

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.