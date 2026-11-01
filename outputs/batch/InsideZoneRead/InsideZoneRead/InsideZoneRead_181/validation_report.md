# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_181`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_181/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [111–126], lower_priority='Action_ZoneBlock' annotated_start=114, effective_Action_ZoneBlock_start=127.
> - Action 'Action_ZoneBlock' range [114-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-195] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-223] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-268] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-297] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-194] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-309] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [154-272] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-168] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [145-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-259] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-77] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-276] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-160] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-328] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-216] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-235] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-303] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-305] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-313] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-329] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-302] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-329] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-325] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-327] for track '38' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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