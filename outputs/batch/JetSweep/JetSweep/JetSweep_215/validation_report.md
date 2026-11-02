# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_215`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_215/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 431: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '2' (TE) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [13–25], lower_priority='Action_ZoneBlock' annotated_start=14, effective_Action_ZoneBlock_start=26.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 137 frames exceeds threshold 90 frames [start=14, end=150].
> - Action 'Action_None' range [13-187] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [14-92] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [94-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-63] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [14-108] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-199] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-208] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-184] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [36-139] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [14-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-184] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-186] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '30' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.