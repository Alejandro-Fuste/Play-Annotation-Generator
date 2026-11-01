# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_197`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_197/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 394: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Segment 'Action_BallCarry' for track '8' has invalid range: start=211, end=107. Clamping end to start.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [171–186], lower_priority='Action_ZoneBlock' annotated_start=174, effective_Action_ZoneBlock_start=187.
> - Action 'Action_None' range [171-192] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-365] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-254] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-208] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [197-204] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-357] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-362] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-240] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-331] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-348] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-389] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '12' starts at frame 187, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [187-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-224] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-311] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-364] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-235] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [240-364] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-378] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-295] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-303] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-336] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-364] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [366-368] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-345] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-369] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-382] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-367] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-374] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-266] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-279] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [236-373] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-312] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-362] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-319] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-363] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-303] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-347] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-331] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-342] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-368] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '35' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.