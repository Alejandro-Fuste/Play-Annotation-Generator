# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_202`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_202/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 141 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [21-286] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [88-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [100-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-280] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-148] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-223] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-246] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-273] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [117-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [156-195] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [199-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [210-212] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [215-219] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [223-226] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [232-234] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [241-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [247-262] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [266-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [274-276] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [279-296] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-150] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-164] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-138] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-214] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-228] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-202] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-223] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-242] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-276] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-115] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-156] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-191] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-230] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-263] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-190] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-220] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-273] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-285] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-295] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-60] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-71] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-102] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-130] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-299] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-256] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-262] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-285] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-106] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-119] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-259] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-280] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-255] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-274] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-52] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-84] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-122] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-162] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-143] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-160] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-177] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-230] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-242] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-261] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-199] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-223] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-229] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-254] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-262] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-283] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-289] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-246] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-266] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-275] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-289] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-297] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-294] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.