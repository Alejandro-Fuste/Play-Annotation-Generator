# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_17`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 148 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Segment 'Action_SnapReceive' for track '4' has invalid range: start=337, end=295. Clamping end to start.
> - Segment 'Action_Handoff' for track '4' has invalid range: start=365, end=295. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '18' has invalid range: start=338, end=159. Clamping end to start.
> - Segment 'Action_BallSnap' for track '19' has invalid range: start=337, end=31. Clamping end to start.
> - Action 'Action_BallCarry' range [379-408] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [413-474] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-426] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [431-432] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-509] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-251] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-288] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-388] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-414] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-481] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [483-488] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-497] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [500-509] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-428] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [346-391] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [395-396] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [398-406] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-211] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-336] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-363] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-367] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-402] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-509] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-445] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-72] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-205] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-262] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-291] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-336] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [337-509] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-436] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-23] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-45] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-193] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-209] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-257] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-287] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-310] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-321] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-336] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-377] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-19] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-105] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-166] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [341-353] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [423-465] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-253] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-282] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-385] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-509] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-7] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-23] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-106] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-140] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-168] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-256] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-282] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-336] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-430] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-166] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-380] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-424] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-310] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-373] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-507] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-509] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [343-345] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-373] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [371-395] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-509] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-390] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-401] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-431] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-497] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [504-505] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-455] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-489] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-494] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-499] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-509] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-504] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.