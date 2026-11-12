# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_181`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_181/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 181 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [158–168], lower_priority='Action_ZoneBlock' annotated_start=161, effective_Action_ZoneBlock_start=169.
> - Action 'Action_None' range [158-337] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-348] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-353] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-358] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-400] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [405-419] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [161-183] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [197-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [203-207] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-284] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-295] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-337] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-364] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-376] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-381] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-386] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-408] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-416] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-207] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-235] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-243] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-336] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-348] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-378] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-384] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-392] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-321] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-419] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-374] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-391] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-211] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-232] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-223] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-359] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [361-362] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-380] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-388] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-399] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-403] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-419] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-261] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-320] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-335] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-364] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-387] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-393] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-401] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [165-247] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-313] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-419] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-297] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-317] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-357] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-389] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-192] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [196-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [209-211] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-316] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-333] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-337] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-389] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-399] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-282] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [161-230] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-321] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-419] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [161-178] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [204-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [231-232] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [234-238] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [243-247] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-417] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-85] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-102] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-111] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [185-334] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [338-339] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [342-363] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [383-384] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-249] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-335] for track '22' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [338-419] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-258] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-268] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-331] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-352] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [297-305] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-332] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-363] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-392] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-418] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-306] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-322] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-411] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [327-328] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-343] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-375] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [377-398] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-418] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-374] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-398] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-419] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-374] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-402] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-414] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [373-374] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-391] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-417] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-398] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-419] for track '34' has 1 frames without a visible bounding box.
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