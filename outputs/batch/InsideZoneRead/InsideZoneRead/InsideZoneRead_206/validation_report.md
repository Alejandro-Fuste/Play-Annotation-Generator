# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_206`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_206/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 125 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '11' has invalid range: start=463, end=381. Clamping end to start.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [460–479], lower_priority='Action_ZoneBlock' annotated_start=463, effective_Action_ZoneBlock_start=480.
> - Segment 'Action_ZoneBlock' for track '21' has invalid range: start=463, end=256. Clamping end to start.
> - Action 'Action_None' range [460-504] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-517] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-527] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-590] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [592-597] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [599-616] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [619-628] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-610] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-604] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [607-610] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [612-616] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [627-628] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-597] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-606] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [608-609] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [613-616] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [618-629] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-598] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [600-629] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-499] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-528] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-537] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-629] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-607] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [613-626] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [460-625] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-629] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-363] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-381] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-612] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-629] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-335] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [463-524] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [526-527] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [531-532] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [535-537] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-606] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [609-610] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-406] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-595] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [597-598] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [601-602] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [610-611] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [484-513] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [514-596] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [599-600] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [602-604] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-629] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [460-479] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [480-486] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-565] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-570] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-595] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [618-619] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [463-510] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [512-543] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-629] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-256] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-267] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-288] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-303] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-629] for track '24' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-345] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-349] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-376] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-481] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-491] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-495] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-501] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-512] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-475] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-479] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-629] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-519] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-556] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-564] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [555-557] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [564-566] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-581] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [577-578] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-584] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-592] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [594-601] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-605] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-629] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-601] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [608-610] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [621-623] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [621-625] for track '41' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.