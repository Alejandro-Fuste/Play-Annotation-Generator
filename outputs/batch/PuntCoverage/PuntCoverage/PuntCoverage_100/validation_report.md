# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_100`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_100/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 177 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 202: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_Tackle' for track '22' has invalid range: start=234, end=220. Clamping end to start.
> - Action 'Action_PreSnap' range [0-73] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-116] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-188] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-200] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-209] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-218] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-192] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-200] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-235] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-299] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-285] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-93] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-123] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-209] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-216] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-34] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-44] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-48] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-95] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-114] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-142] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-131] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-272] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-284] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-33] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-74] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-252] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-284] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-293] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-272] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-244] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-250] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-122] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-137] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-34] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-150] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-209] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-216] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-131] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-201] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-220] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-144] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-153] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-172] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-185] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-288] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-113] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-195] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-213] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-230] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-299] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-202] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-213] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-221] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-246] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-201] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-220] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-235] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-245] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-258] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-266] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [206-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-196] for track '30' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-224] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-291] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-198] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-211] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-220] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-218] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-221] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-227] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-235] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-243] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-218] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-237] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-284] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-237] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-247] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-254] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-269] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-285] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-243] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-253] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-268] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-293] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-260] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-270] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-286] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-290] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-285] for track '45' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.