# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_133`
- **Input XML**: `outputs/batch/Power/Power/Power_133/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 48 |
| Player Tracks | 48 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 268: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 268: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [0-289] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-362] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-367] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-262] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-360] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-383] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [385-396] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-403] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-410] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-260] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-265] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-280] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-419] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [203-211] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [252-256] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-419] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-260] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-402] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-405] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-30] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-287] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-300] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-319] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-329] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-338] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [203-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [203-255] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-192] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-238] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-419] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-316] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-289] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-296] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-327] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-302] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-354] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-358] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-366] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-369] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-378] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-389] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-418] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-389] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-397] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-404] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [408-415] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-404] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-418] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-407] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-410] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-418] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-407] for track '47' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.