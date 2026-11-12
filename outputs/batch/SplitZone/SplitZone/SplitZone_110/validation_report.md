# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_110`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_110/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [188–203], lower_priority='Action_ZoneBlock' annotated_start=191, effective_Action_ZoneBlock_start=204.
> - Action 'Action_BallCarry' range [222-407] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [411-417] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-289] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-297] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-326] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-345] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-419] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-290] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-227] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-267] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-286] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-388] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [390-408] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [198-267] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-384] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-254] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-283] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-318] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-419] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-14] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-264] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-306] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-316] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-341] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-388] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-406] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-315] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-242] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-289] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-419] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-304] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-341] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [347-361] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [377-407] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-416] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-419] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-270] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-380] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-413] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-295] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-419] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-307] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-406] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-382] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-382] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [393-405] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-354] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-363] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-370] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-350] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-360] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-385] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-390] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [391-401] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-410] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-419] for track '39' has 2 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.