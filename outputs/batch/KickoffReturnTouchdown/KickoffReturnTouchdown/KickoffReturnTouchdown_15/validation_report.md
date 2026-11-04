# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_15`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 68 |
| Player Tracks | 68 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 239 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 689 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 32: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
> - Segment 'Action_KickBall' for track '9' has invalid range: start=187, end=167. Clamping end to start.
> - Segment 'Action_CrossGoalLine' for track '36' has invalid range: start=678, end=388. Clamping end to start.
> - Action 'Action_None' range [124-689] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-375] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-656] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-372] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-398] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-640] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-406] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-412] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-424] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-434] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [439-456] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [458-460] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-498] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-506] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-543] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [546-689] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-215] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-282] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-294] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [296-310] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-289] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-316] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-624] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [626-636] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [639-673] for track '5' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [124-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-372] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-567] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [572-574] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-580] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [582-605] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [608-611] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [618-619] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [621-630] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [652-658] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [660-678] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [124-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-273] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [280-348] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-364] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-399] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-660] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-196] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-16] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-20] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-156] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-118] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-244] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-260] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-306] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-344] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [346-359] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [392-394] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-397] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-289] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-306] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-319] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-554] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-230] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-267] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-302] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-515] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [210-221] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-244] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-498] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-368] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-395] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-631] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-238] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-252] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [256-291] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [296-310] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-314] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-328] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-348] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-514] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [517-554] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [557-567] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-578] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [581-597] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [601-602] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-631] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [633-650] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-247] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-249] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [331-388] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-291] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-277] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-306] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [309-385] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-558] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [560-612] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-274] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-318] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-378] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-309] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-344] for track '42' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [355-362] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-470] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-480] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-491] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-522] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-541] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [543-548] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [361-436] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-611] for track '44' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [614-626] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [628-675] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-396] for track '45' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [370-426] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-381] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-655] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [386-412] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-426] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-617] for track '49' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [402-419] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-491] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-511] for track '51' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [513-517] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-524] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [527-682] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-505] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [554-555] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-466] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-471] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-478] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-491] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-496] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-505] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [513-515] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-689] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-479] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-493] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-642] for track '56' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [521-522] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-536] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-548] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-560] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-535] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [534-535] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [537-546] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-624] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-545] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-548] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-554] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [558-568] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [571-572] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-583] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [585-586] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [589-590] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [593-597] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [600-614] for track '62' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [549-550] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-586] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-602] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [604-689] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [622-626] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-629] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [631-632] for track '66' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.