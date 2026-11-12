# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_240`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_240/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 35 |
| Ball Tracks | 2 |
| CSV events parsed | 20 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [114–127], lower_priority='Action_ZoneBlock' annotated_start=117, effective_Action_ZoneBlock_start=128.
> - Action 'Action_None' range [114-252] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-196] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-365] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-256] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-391] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-401] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-403] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [147-229] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [233-242] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [246-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-335] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-344] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-407] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [122-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [155-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-203] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [163-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-338] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-352] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-412] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [114-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-276] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-316] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-332] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-340] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-358] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [128-147] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-258] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-273] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [275-278] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-358] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-291] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-223] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-283] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-291] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-344] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-184] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-318] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [332-339] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-279] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-310] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-327] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [335-347] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-322] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-391] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-327] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-363] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-306] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-419] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-360] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-380] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-392] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-355] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-372] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [389-406] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-416] for track '36' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.