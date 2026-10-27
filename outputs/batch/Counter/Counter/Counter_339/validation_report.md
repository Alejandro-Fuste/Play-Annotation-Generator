# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_339`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_339/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 680: Duplicate assignment for track ID '22' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [76–87], lower_priority='Action_DownBlock' annotated_start=79, effective_Action_DownBlock_start=88.
> - Validation warning: Action 'Action_PullBlock' for track '19' (DT1) duration 116 frames exceeds threshold 90 frames [start=79, end=194].
> - Action 'Action_None' range [76-222] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-223] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-202] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-224] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-30] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-37] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [85-111] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-132] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-101] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-193] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-237] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [76-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [83-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [123-149] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 76, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [76-80] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-151] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-220] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-19] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-41] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-19] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [79-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [94-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-15] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-108] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-32] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [82-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [116-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [95-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [115-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [153-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-172] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-220] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-228] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-239] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-203] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-213] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-238] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-217] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '31' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.