# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_165`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_165/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 104 frames exceeds threshold 90 frames [start=123, end=226].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (RG) duration 104 frames exceeds threshold 90 frames [start=123, end=226].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 94 frames exceeds threshold 90 frames [start=123, end=216].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 104 frames exceeds threshold 90 frames [start=123, end=226].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [121–129], lower_priority='Action_ZoneBlock' annotated_start=123, effective_Action_ZoneBlock_start=130.
> - Action 'Action_None' range [121-403] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [121-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-342] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [410-418] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-427] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-316] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-278] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-281] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-262] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-216] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-271] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-213] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-262] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-274] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-120] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-146] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-190] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-216] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-381] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-333] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-282] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-320] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-339] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-248] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-449] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-374] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-393] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-409] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [430-431] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-301] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-313] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-365] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-396] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-328] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-434] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-314] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-343] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-352] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-386] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-419] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-336] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-300] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-342] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-419] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-428] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-431] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-378] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-449] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-401] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-443] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-405] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-400] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-423] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-416] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-419] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-446] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [412-418] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-436] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-438] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-448] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-441] for track '42' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.