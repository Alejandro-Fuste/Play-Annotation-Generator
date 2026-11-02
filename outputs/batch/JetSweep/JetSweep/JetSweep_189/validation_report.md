# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_189`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_189/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 135 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [58–71], lower_priority='Action_ZoneBlock' annotated_start=60, effective_Action_ZoneBlock_start=72.
> - Action 'Action_JetMotion' range [1-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [268-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-212] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-280] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-205] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-268] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [271-286] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-181] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-219] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-329] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-87] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-195] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-264] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-283] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-312] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-325] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-296] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-312] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-270] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-296] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-303] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-310] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-329] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-252] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-329] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-231] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-325] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-27] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-66] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-98] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-147] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-207] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-226] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-267] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-276] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-285] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-237] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-256] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-294] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-312] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-306] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-313] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-311] for track '35' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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