# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_191`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_191/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 85 |
| Player Tracks | 85 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 235 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [49–58], lower_priority='Action_ZoneBlock' annotated_start=53, effective_Action_ZoneBlock_start=59.
> - Action 'Action_BallCarry' range [72-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-140] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-260] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-267] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [271-272] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [274-281] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [284-304] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [307-308] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [313-316] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [320-324] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [328-330] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [335-340] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-202] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [53-117] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-83] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-208] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-222] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-293] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-305] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-330] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-202] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-164] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-325] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-330] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-106] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-93] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-211] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-285] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-305] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-346] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [16-139] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [141-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [161-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-232] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-241] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-224] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-187] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-172] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-114] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-202] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-330] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-83] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-177] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-254] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-261] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-330] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-246] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-229] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-243] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [245-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-213] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-181] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-209] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-199] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-193] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-199] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-221] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-208] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-223] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-226] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-266] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-278] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-330] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-233] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-248] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-265] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-278] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-300] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-305] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-316] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-341] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-347] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-263] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-246] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-263] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-304] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-330] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-255] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-271] for track '53' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-293] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-304] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-307] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-318] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-336] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-348] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-335] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-302] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-315] for track '64' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-343] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-298] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-324] for track '66' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-304] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-330] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-307] for track '68' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-315] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-330] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-359] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-323] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-320] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-347] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-324] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-350] for track '76' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-341] for track '78' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-350] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-338] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-343] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-355] for track '82' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-358] for track '83' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-358] for track '84' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.