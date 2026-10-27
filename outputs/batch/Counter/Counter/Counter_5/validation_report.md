# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_5`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 11: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 12: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [57–71], lower_priority='Action_DownBlock' annotated_start=63, effective_Action_DownBlock_start=72.
> - Action 'Action_PullLeadBlock' range [63-121] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [123-129] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-269] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-142] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-102] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [63-102] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-103] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-249] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [92-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [166-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [57-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [85-91] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-136] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-152] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [63-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [101-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [116-133] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [63-99] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [101-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-189] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [57-103] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-124] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-148] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [111-133] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-184] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-269] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-238] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-213] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-214] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '38' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.