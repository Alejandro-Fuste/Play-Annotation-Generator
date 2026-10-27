# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_227`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_227/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [45–60], lower_priority='Action_DownBlock' annotated_start=48, effective_Action_DownBlock_start=61.
> - Action 'Action_None' range [45-212] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [48-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [97-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [108-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-175] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-161] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-184] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-67] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-88] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [53-81] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [83-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [48-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-114] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-233] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [61-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [48-108] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [132-239] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-224] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-184] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-207] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [209-223] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-236] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-209] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '35' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.