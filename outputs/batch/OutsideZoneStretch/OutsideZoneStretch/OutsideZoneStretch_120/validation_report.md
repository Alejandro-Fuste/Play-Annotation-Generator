# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_120`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_120/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 130 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 242: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Action 'Action_None' range [87-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-214] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-208] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-479] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-291] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-248] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-297] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-302] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-196] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-305] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-323] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [45-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-449] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-461] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-245] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-227] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-281] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-183] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-250] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-366] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-376] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-249] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-259] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-312] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-160] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-274] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-223] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-333] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-241] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-327] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-231] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-273] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-279] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-238] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-274] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-470] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-231] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-276] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-266] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-317] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-321] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-298] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-316] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-368] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [371-378] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-382] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-336] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-448] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-348] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-351] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [371-412] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-432] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-451] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-459] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [461-462] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [469-475] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-404] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-479] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-376] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-444] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [410-436] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-435] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [424-451] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [441-454] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [458-459] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [461-464] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [463-474] for track '44' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.