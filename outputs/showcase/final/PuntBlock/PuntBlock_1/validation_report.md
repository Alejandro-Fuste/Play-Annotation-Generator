# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_1`
- **Input XML**: `output_showcase_final/PuntBlock/PuntBlock_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 89 |
| Player Tracks | 89 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 294 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 4: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 4: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureRecovery' for track '7' has invalid range: start=233, end=45. Clamping end to start.
> - Action 'Action_None' range [1-167] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-202] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-280] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-31] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-42] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-91] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-134] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-86] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-40] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-69] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-146] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-282] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [286-291] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-94] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-129] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-46] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-68] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [72-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-51] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-100] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-172] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-278] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-111] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-212] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [218-284] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-62] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-212] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-254] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-299] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [1-51] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [48-78] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [82-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [126-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [1-46] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-132] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-27] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-75] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-106] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-122] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-139] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-223] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-133] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [59-68] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-74] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-110] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-134] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-72] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-74] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-133] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-142] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-104] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-129] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-243] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-105] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-254] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-281] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-98] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-253] for track '33' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [274-280] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-136] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-131] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-156] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-170] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-202] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-225] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-152] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-151] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-181] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-212] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-258] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-176] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '47' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-211] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-252] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-277] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-169] for track '48' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-203] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-252] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-296] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-299] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-211] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-249] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-278] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-299] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-257] for track '65' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-281] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-285] for track '66' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '68' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '69' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-278] for track '69' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '71' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-288] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-283] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-275] for track '76' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '79' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-299] for track '79' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '80' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '80' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-279] for track '81' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '81' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '82' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '83' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '83' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '84' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '84' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '84' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '84' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '85' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-298] for track '87' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-299] for track '88' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.