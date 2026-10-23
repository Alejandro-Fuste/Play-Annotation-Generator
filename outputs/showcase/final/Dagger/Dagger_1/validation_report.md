# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_1`
- **Input XML**: `output_showcase_final/Dagger/Dagger_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 137 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [158–174], lower_priority='Action_PassBlock' annotated_start=161, effective_Action_PassBlock_start=175.
> - Action 'Action_BreakInside' range [174-297] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-332] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-360] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-278] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-377] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [161-252] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [256-267] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [270-272] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [276-280] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [283-290] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [293-294] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [296-314] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [332-334] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [339-340] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-242] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [244-252] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-258] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-368] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-337] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-351] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-331] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-349] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-379] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-388] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [161-291] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [293-315] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [324-325] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-234] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [236-260] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-389] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [175-242] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [245-248] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [250-266] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [270-271] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [276-278] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [281-282] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [284-301] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [308-310] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-372] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-293] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-389] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [260-268] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-314] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-381] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [383-389] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-272] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-250] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-289] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [158-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-389] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [161-203] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [161-186] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [189-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [198-385] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-267] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-294] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [296-321] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-329] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-335] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-294] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-321] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [324-333] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-340] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-279] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-322] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-353] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-369] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-389] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-315] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-314] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-386] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-334] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [337-340] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-356] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-369] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '35' has 1 frames without a visible bounding box.
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