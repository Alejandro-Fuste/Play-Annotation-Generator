# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_52`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [82–91], lower_priority='Action_ZoneBlock' annotated_start=84, effective_Action_ZoneBlock_start=92.
> - Action 'Action_BallCarry' range [115-260] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-224] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-216] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-221] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-262] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [82-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-99] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '21' starts at frame 84, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [84-158] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-87] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-204] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-221] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-236] for track '31' has 2 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.