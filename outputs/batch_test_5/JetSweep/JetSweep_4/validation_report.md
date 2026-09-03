# TapeVision Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_4`
- **Input XML**: `outputs/batch_test_5/JetSweep/JetSweep_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 27 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=115, end=110. Clamping end to start.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [115–115], lower_priority='Action_ZoneBlock' annotated_start=115, effective_Action_ZoneBlock_start=116.
> - Action 'Action_None' range [73-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-146] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '3' starts at frame 155, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [155-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-242] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-154] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 155, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [155-155] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-85] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-207] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-329] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [73-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [90-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [126-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-359] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-280] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-149] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-234] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-301] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-323] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-274] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-357] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-274] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-359] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-319] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-333] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-277] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-354] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-284] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-309] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-305] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-317] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-354] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-359] for track '37' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.