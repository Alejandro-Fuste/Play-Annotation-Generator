# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_32`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 66 |
| Player Tracks | 65 |
| Ball Tracks | 1 |
| CSV events parsed | 20 |
| Action Segments inferred | 135 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 66: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '0' (C): higher_priority='Action_BallSnap' [215–229], lower_priority='Action_ZoneBlock' annotated_start=218, effective_Action_ZoneBlock_start=230.
> - Action 'Action_ZoneBlock' range [230-280] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-310] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-335] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-354] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [218-289] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-331] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-284] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-265] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-308] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [218-293] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [295-296] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [298-300] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [218-232] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-336] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [227-261] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-298] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [242-267] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-291] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-429] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-438] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-303] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-355] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-255] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-275] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-354] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-276] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-306] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-357] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [268-297] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-302] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-449] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-302] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-296] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-305] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-285] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-296] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-304] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-344] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-449] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-368] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-368] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-367] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-384] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-409] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-367] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-378] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-371] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-377] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-394] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [406-409] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-427] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-444] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [446-449] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-376] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-381] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-382] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-443] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [380-382] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-382] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-410] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-383] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-395] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-404] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-407] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-420] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-423] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-409] for track '42' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [388-393] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-400] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-397] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-401] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-404] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-435] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-445] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-410] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-420] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-416] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-421] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-426] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-438] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-409] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-416] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [419-429] for track '56' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [432-449] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-443] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-440] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-449] for track '62' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.