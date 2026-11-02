# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_20`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 53 |
| Player Tracks | 53 |
| Ball Tracks | 0 |
| CSV events parsed | 27 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 42: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [57–70], lower_priority='Action_ZoneBlock' annotated_start=61, effective_Action_ZoneBlock_start=71.
> - Segment 'Action_BallCarry' for track '16' has invalid range: start=91, end=84. Clamping end to start.
> - Action 'Action_LeadBlock' range [61-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-119] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-124] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [57-116] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-196] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-174] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [129-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [65-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-147] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-216] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-233] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-209] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-239] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-212] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-209] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-205] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-222] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-238] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-229] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-237] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-239] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '49' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.