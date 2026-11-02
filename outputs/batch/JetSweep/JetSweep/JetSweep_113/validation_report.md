# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_113`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_113/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 228: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 107 frames exceeds threshold 90 frames [start=56, end=162].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 107 frames exceeds threshold 90 frames [start=56, end=162].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 107 frames exceeds threshold 90 frames [start=56, end=162].
> - Validation warning: Action 'Action_LeadBlock' for track '11' (TE2) duration 107 frames exceeds threshold 90 frames [start=56, end=162].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [54–71], lower_priority='Action_ZoneBlock' annotated_start=56, effective_Action_ZoneBlock_start=72.
> - Action 'Action_None' range [54-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-158] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-199] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-71] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-163] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-73] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [51-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-132] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-181] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-179] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-146] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-154] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-166] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '31' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.