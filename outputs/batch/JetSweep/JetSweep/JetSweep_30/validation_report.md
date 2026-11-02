# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_30`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 27 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [103–116], lower_priority='Action_ZoneBlock' annotated_start=108, effective_Action_ZoneBlock_start=117.
> - Action 'Action_PreSnap' range [0-60] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-253] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-162] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-260] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-116] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 103, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [103-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [140-169] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [106-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [135-246] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-251] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-177] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-167] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-220] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-229] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-223] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-269] for track '34' has 1 frames without a visible bounding box.
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