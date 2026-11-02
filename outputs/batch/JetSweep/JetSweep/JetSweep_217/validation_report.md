# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_217`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_217/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '3' (TE) duration 111 frames exceeds threshold 90 frames [start=114, end=224].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 111 frames exceeds threshold 90 frames [start=114, end=224].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 111 frames exceeds threshold 90 frames [start=114, end=224].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [113–127], lower_priority='Action_ZoneBlock' annotated_start=114, effective_Action_ZoneBlock_start=128.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 97 frames exceeds threshold 90 frames [start=114, end=210].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 111 frames exceeds threshold 90 frames [start=114, end=224].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 111 frames exceeds threshold 90 frames [start=114, end=224].
> - Action 'Action_None' range [113-173] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [137-292] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [128-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-163] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-296] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-224] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-184] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-185] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-259] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-294] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.