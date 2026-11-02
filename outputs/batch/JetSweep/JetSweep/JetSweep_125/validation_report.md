# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_125`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_125/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 98 frames exceeds threshold 90 frames [start=69, end=166].
> - Validation warning: Action 'Action_LeadBlock' for track '12' (QB) duration 98 frames exceeds threshold 90 frames [start=69, end=166].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [68–80], lower_priority='Action_ZoneBlock' annotated_start=69, effective_Action_ZoneBlock_start=81.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 98 frames exceeds threshold 90 frames [start=69, end=166].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 98 frames exceeds threshold 90 frames [start=69, end=166].
> - Action 'Action_None' range [68-170] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [99-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-221] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-223] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [102-153] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [167-234] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [69-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-239] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [68-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-107] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-232] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '21' starts at frame 69, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [69-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-146] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-178] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-184] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-220] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-239] for track '28' has 1 frames without a visible bounding box.
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