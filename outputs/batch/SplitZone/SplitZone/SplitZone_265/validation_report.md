# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_265`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_265/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 145 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 532: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 532: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 99 frames exceeds threshold 90 frames [start=134, end=232].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 99 frames exceeds threshold 90 frames [start=134, end=232].
> - Validation warning: Action 'Action_ZoneBlock' for track '22' (RT) duration 99 frames exceeds threshold 90 frames [start=134, end=232].
> - Action 'Action_PreSnap' range [26-211] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-248] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-266] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-277] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-283] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-207] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-218] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-293] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-331] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-341] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-321] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [170-397] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [399-418] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-390] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-186] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-235] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-280] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-376] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-385] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-187] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-303] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-349] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-358] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-366] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-330] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-366] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-377] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-382] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-389] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-398] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-406] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [141-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [153-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [165-199] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-261] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-288] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-294] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-356] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-374] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-336] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-231] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [233-382] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-413] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-217] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-332] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-342] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-391] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-145] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-160] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-220] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [224-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [231-232] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-379] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [396-397] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-407] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-415] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-59] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-82] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-242] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-254] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-270] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-334] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-55] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-189] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-226] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-330] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-287] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [163-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [169-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-389] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-399] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-417] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-275] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-348] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-393] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-410] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-227] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-288] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-351] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-356] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-381] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-390] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-400] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-407] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-317] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-349] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-376] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-392] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-410] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-366] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-374] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-345] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-407] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-356] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-419] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [385-391] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-407] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-417] for track '34' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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