# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_214`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_214/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 127 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 430: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (RG) duration 94 frames exceeds threshold 90 frames [start=88, end=181].
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 94 frames exceeds threshold 90 frames [start=88, end=181].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [87–100], lower_priority='Action_ZoneBlock' annotated_start=88, effective_Action_ZoneBlock_start=101.
> - Action 'Action_None' range [87-147] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-123] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-142] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-152] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-174] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [88-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [161-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-98] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-112] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-120] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-208] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-132] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-155] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-12] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-19] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-131] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-193] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [89-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [123-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-160] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-142] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-167] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-198] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-241] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-245] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-267] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-269] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-208] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-220] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-226] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-263] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-261] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '41' has 1 frames without a visible bounding box.
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