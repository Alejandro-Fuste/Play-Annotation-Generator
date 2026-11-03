# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_62`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 52 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 174 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [6-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-189] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-262] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-274] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-56] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-107] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-217] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-283] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-329] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [6-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-148] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-235] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-263] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [64-69] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-78] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-139] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [6-38] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-215] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-224] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-241] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-293] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [307-311] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-146] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-204] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-243] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-267] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-277] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [57-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-13] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [6-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-273] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [275-283] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [285-329] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-36] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-49] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-35] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-43] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-172] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-122] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [53-186] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-275] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-315] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-150] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [152-276] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [61-144] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-240] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-270] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-306] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-220] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-153] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-282] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-304] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-282] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-306] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-232] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-126] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-202] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-129] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-147] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-207] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-226] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-329] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-142] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-295] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-166] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-197] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-236] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-203] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-212] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-225] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-271] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-231] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-222] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-226] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-225] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-280] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-266] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-280] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-257] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-264] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-282] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-318] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-329] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-329] for track '51' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.