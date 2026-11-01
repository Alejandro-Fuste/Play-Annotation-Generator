# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_118`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_118/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [245–261], lower_priority='Action_ZoneBlock' annotated_start=248, effective_Action_ZoneBlock_start=262.
> - Action 'Action_PreSnap' range [0-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-427] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-349] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-360] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-353] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [300-368] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [370-438] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-443] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-449] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-370] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-272] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-292] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-273] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-60] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-88] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-163] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-302] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-323] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-449] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-340] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-350] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-374] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-331] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-361] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-365] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-385] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-402] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-421] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-419] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-415] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-421] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-430] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-438] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-445] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-449] for track '33' has 3 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.