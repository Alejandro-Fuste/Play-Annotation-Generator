# TapeVision Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_5`
- **Input XML**: `outputs/batch_test_5/JetSweep/JetSweep_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 26 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 12: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [88–101], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=102.
> - Action 'Action_BallCarry' range [117-224] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-127] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-308] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-188] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-316] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-292] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [88-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-160] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-116] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-166] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-234] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-303] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-329] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-307] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-325] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-176] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [88-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-112] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-61] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-260] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-229] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-284] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-329] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-329] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [238-273] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-329] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-329] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-273] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '41' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.