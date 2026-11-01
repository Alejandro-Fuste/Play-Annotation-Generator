# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_108`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_108/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '9' has invalid range: start=156, end=109. Clamping end to start.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [153–167], lower_priority='Action_ZoneBlock' annotated_start=156, effective_Action_ZoneBlock_start=168.
> - Action 'Action_None' range [153-206] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-267] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-216] for track '1' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [236-389] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-389] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-260] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-223] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-280] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [170-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [200-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [218-222] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [229-263] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [200-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-251] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-265] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-206] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-389] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-193] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [178-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-389] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-106] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-254] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-271] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-280] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-252] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-272] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-278] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-287] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-321] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-389] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-305] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-309] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-329] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-321] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-357] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-386] for track '37' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.