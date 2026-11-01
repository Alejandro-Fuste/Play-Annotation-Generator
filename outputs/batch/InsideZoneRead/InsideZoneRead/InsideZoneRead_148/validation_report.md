# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_148`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_148/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 58 |
| Player Tracks | 58 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 155 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 296: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 92 frames exceeds threshold 90 frames [start=321, end=412].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 92 frames exceeds threshold 90 frames [start=321, end=412].
> - Resolved action overlap for track '22' (C): higher_priority='Action_BallSnap' [318–334], lower_priority='Action_ZoneBlock' annotated_start=321, effective_Action_ZoneBlock_start=335.
> - Action 'Action_None' range [318-374] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-379] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-421] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-430] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [432-433] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-438] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-539] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-412] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-410] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-384] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-393] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [321-347] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 413, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [413-415] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-364] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-482] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-358] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-377] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-393] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-397] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-410] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-473] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-480] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-484] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-539] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [363-429] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [431-433] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [438-443] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [445-499] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [532-539] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-430] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-442] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [321-338] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [348-353] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-433] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-539] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [318-391] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-404] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-412] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-448] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [453-454] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-459] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-469] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-491] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [496-497] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [321-335] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-395] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-46] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-104] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-409] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [335-351] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [355-360] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [363-364] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-31] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-55] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-185] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-369] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-376] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-423] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [425-539] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-364] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-397] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [399-455] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [459-460] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-539] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-404] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-412] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-426] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-438] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-403] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-415] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [425-430] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-539] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-411] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-426] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-418] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-434] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-420] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-435] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [428-430] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-443] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-539] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-539] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-454] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-539] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-524] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-454] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-460] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-489] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-479] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [478-480] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-539] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-500] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-539] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-539] for track '57' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.