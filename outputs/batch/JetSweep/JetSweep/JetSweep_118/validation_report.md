# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_118`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_118/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 238: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [34–48], lower_priority='Action_ZoneBlock' annotated_start=35, effective_Action_ZoneBlock_start=49.
> - Action 'Action_None' range [34-173] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-195] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-149] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-171] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [60-209] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-80] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-172] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-151] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-191] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-69] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-52] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [35-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '27' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.