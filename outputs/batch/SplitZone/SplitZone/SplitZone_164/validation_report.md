# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_164`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_164/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [161–172], lower_priority='Action_ZoneBlock' annotated_start=164, effective_Action_ZoneBlock_start=173.
> - Action 'Action_None' range [161-197] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-261] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-256] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-307] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-360] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-375] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [179-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-280] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-148] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '7' starts at frame 238, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [238-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-242] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-181] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-204] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-248] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [173-187] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-222] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-259] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [168-194] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [197-215] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [219-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-93] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-199] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-184] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-275] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-189] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-204] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-207] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [226-233] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-304] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-372] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-248] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-251] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-271] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-321] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-370] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-335] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-324] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-351] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-361] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-347] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.