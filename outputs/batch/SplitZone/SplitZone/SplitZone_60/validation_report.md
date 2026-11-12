# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_60`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 136 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 123 frames exceeds threshold 90 frames [start=178, end=300].
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 96 frames exceeds threshold 90 frames [start=178, end=273].
> - Segment 'Action_BlockSecondLevel' for track '12' has invalid range: start=205, end=198. Clamping end to start.
> - Action 'Action_None' range [301-396] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-318] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-280] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [283-317] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-323] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-363] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-369] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [203-213] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [221-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [230-261] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [274-333] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [341-415] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [178-261] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [265-273] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-161] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-299] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [304-340] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-357] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-419] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-277] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-413] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-27] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-36] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-62] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-110] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-131] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-268] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [271-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-375] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-394] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-211] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-274] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-357] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [361-380] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-271] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-16] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-28] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-40] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-83] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [178-192] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-133] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [181-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-291] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-419] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-247] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-223] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-403] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-413] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-262] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-264] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-315] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-344] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-410] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-292] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-343] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-407] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [281-394] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [400-403] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-309] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-320] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-328] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-334] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-344] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-361] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-375] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-386] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-419] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-321] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-383] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-337] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-351] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-339] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-390] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-375] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-375] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-394] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-383] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-403] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-413] for track '31' has 2 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.