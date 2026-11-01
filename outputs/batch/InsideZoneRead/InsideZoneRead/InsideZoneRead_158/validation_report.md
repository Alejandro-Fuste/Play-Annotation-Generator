# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_158`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_158/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 316: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 316: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [324–337], lower_priority='Action_ZoneBlock' annotated_start=327, effective_Action_ZoneBlock_start=338.
> - Action 'Action_None' range [324-478] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-350] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-468] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-350] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-425] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-520] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [324-504] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-520] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-395] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-457] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [362-529] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-529] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-341] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-382] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-443] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-344] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [327-371] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [376-377] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-499] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-137] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-157] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-298] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-321] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [327-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-338] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-405] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-411] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-434] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-439] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [327-347] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [363-367] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-323] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [324-326] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [328-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [335-336] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [340-341] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [353-359] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [368-383] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-16] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-126] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [324-352] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [327-335] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-66] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-371] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-444] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-471] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-495] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [499-509] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-539] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [469-491] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-509] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [508-509] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-514] for track '34' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.