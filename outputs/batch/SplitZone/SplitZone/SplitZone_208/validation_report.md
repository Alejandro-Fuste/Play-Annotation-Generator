# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_208`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_208/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 143 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 95 frames exceeds threshold 90 frames [start=193, end=287].
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 95 frames exceeds threshold 90 frames [start=193, end=287].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 95 frames exceeds threshold 90 frames [start=193, end=287].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [190–201], lower_priority='Action_ZoneBlock' annotated_start=193, effective_Action_ZoneBlock_start=202.
> - Action 'Action_PreSnap' range [27-189] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-233] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-301] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-448] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-243] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [216-245] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [251-255] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [268-275] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-320] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-403] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [215-223] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [232-316] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [320-337] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-35] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-204] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [207-287] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-343] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-376] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-381] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [199-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [209-211] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [228-233] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-40] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-79] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-51] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-36] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-219] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [228-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-265] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-281] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-50] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-34] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-53] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [202-223] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [227-238] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-311] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-364] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-246] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-370] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-42] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-52] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-203] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-166] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-221] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-241] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-298] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-325] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-226] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-240] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-267] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-291] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-224] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-287] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-220] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-249] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-261] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-309] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-429] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-260] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-342] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-400] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [408-416] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-350] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-324] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-398] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-416] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-363] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-374] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-311] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-443] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-353] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-367] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-405] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-426] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-350] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-427] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-403] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-378] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-391] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-435] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-442] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-448] for track '44' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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