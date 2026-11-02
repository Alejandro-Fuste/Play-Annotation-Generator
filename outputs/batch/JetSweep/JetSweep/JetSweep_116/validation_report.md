# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_116`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_116/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [143–155], lower_priority='Action_ZoneBlock' annotated_start=145, effective_Action_ZoneBlock_start=156.
> - Action 'Action_None' range [143-166] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-177] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-255] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-263] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [145-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-273] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-213] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-310] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-237] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-289] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-326] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-169] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-191] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-169] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-166] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-174] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-231] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-288] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-316] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-266] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-284] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-294] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [271-273] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-303] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '37' has 1 frames without a visible bounding box.
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