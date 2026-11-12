# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_229`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_229/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 137 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 460: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [121–125], lower_priority='Action_ZoneBlock' annotated_start=124, effective_Action_ZoneBlock_start=126.
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 104 frames exceeds threshold 90 frames [start=124, end=227].
> - Segment 'Action_ZoneBlock' for track '16' has invalid range: start=124, end=83. Clamping end to start.
> - Action 'Action_None' range [121-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-170] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-292] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-182] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [187-189] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-215] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [221-235] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-283] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-215] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-169] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [139-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [165-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [174-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [182-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [202-215] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-242] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-238] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [163-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-7] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-91] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-17] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-193] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-248] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-288] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [201-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-278] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-83] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-214] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [219-287] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-298] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-236] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-253] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-281] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-296] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-235] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-211] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-234] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-255] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-250] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-283] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-294] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-269] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-271] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-283] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-276] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-299] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '44' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.