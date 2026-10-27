# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_377`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_377/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 52 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 236 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 756: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_DownBlock' for track '13' has invalid range: start=106, end=105. Clamping end to start.
> - Action 'Action_None' range [103-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-213] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-295] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-148] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-150] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-189] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-152] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-149] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [106-140] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [106-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [121-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [141-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-166] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-115] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-158] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-225] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-268] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [270-281] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-298] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [134-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [106-186] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-229] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [156-165] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [167-186] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-232] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [239-255] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [258-259] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-147] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-205] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-194] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-265] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-286] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-35] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-81] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-101] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-195] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-214] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-279] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-144] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-177] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-116] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-194] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [196-221] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-234] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-255] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-298] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-11] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-116] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-23] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-89] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [106-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [125-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [128-129] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [132-174] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-175] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-252] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [254-264] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-278] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-296] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-192] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-264] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-272] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-298] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-142] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-158] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-202] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-248] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-264] for track '30' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-299] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-188] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-218] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-231] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-245] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-275] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-194] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-207] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-214] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-299] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-171] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-199] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-222] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-293] for track '37' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-263] for track '39' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-276] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-288] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-298] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-243] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-288] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-299] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-263] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-298] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-268] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-281] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-299] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-284] for track '45' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-281] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-299] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '51' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.