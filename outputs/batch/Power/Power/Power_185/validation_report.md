# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_185`
- **Input XML**: `outputs/batch/Power/Power/Power_185/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 154 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [26-317] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-200] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-277] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-179] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-215] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-229] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-87] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-165] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-292] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-306] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-81] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-88] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-318] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-323] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-102] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-165] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-168] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [80-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-129] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [133-136] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-290] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-302] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-114] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-133] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-145] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-329] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [80-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [90-97] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [99-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [105-134] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-116] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-159] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-165] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-199] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-313] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-324] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-329] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-100] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [80-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [92-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [130-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-124] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-139] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-156] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-178] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-102] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-143] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-165] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-270] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-123] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-159] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-281] for track '25' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-144] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-185] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-217] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-226] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-241] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-259] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-158] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-180] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-196] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-215] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-317] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-329] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-165] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-179] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-200] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-233] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-243] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-292] for track '32' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-188] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-196] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-214] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-268] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-284] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-297] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-329] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-200] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-211] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-240] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-260] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-329] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-196] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-225] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-233] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-241] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-278] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-329] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-281] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-288] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-303] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-317] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-305] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-329] for track '44' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.