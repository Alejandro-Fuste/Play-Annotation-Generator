# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_47`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 67 |
| Player Tracks | 67 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 310 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 96: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SnapReceive' for track '26' has invalid range: start=97, end=85. Clamping end to start.
> - Action 'Action_None' range [52-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-216] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-250] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-298] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-308] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-380] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-392] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-401] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-500] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [503-509] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [513-551] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [553-568] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [271-536] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [539-541] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-110] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-189] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-213] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-236] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-380] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-395] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-401] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-427] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [429-440] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-449] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-569] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-136] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-149] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-223] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-267] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-105] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-262] for track '10' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [264-277] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-279] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-296] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-521] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-534] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [537-543] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [551-569] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-195] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-208] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-223] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [52-206] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [52-144] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [52-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-214] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-277] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-16] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-83] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-125] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-380] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [413-512] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-522] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-84] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-128] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-183] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-32] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-72] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-476] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [488-517] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-521] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-69] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-145] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-183] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-431] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [433-441] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-448] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-456] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-462] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-470] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [474-525] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-203] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-121] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-140] for track '28' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-155] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-224] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-269] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-550] for track '31' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [156-567] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-182] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-215] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-260] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-345] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-439] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [465-518] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-542] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-194] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-213] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-243] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-225] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-241] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-258] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-282] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-298] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-307] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-222] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-384] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-391] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-400] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-413] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-429] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [431-432] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-436] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-458] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-529] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-542] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [550-551] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-262] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-435] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-250] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-271] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-314] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-246] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-262] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-277] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-298] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-318] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-393] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-409] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-290] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-298] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-374] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-391] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-407] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-383] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-403] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [405-481] for track '50' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [483-501] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [503-548] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-307] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-324] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-346] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-323] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-373] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-381] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-569] for track '53' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [313-319] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-398] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-341] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-360] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-374] for track '58' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [376-380] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-391] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-395] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-401] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-547] for track '58' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [550-551] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-412] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-426] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-440] for track '59' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [448-515] for track '59' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-407] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-453] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-401] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-410] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-412] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-436] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [445-455] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-489] for track '62' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [494-498] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-431] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-441] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [443-446] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-460] for track '63' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [480-523] for track '64' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [540-542] for track '65' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.