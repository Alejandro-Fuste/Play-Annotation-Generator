# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_128`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_128/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 50 |
| Player Tracks | 50 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 258: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [10–23], lower_priority='Action_ZoneBlock' annotated_start=12, effective_Action_ZoneBlock_start=24.
> - Segment 'Action_BallCarry' for track '19' has invalid range: start=41, end=11. Clamping end to start.
> - Action 'Action_None' range [10-84] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-68] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-44] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-65] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-76] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-111] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-65] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-211] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-41] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-107] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [12-42] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [61-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-49] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-121] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-165] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-27] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-86] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [3-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-21] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-36] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-68] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-64] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-123] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-129] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-71] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-132] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-186] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-128] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-133] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-139] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-160] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-167] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-195] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-236] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-215] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-229] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-229] for track '49' has 2 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.