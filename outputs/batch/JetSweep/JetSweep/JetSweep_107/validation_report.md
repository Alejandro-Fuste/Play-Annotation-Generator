# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_107`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_107/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [132–154], lower_priority='Action_ZoneBlock' annotated_start=135, effective_Action_ZoneBlock_start=155.
> - Action 'Action_None' range [132-195] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-280] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-356] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-169] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-204] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-204] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-166] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [135-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-336] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 220, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [220-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-195] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [202-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-154] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-200] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [178-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-248] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [251-309] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [311-313] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-237] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-256] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-359] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-243] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-257] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-293] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-318] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-327] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-273] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-289] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-339] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-313] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-336] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-309] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-334] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-336] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-359] for track '43' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.