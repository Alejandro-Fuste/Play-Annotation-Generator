# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_345`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_345/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 691: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 692: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 692: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '2' (C) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
> - Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [22–36], lower_priority='Action_DownBlock' annotated_start=25, effective_Action_DownBlock_start=37.
> - Validation warning: Action 'Action_DownBlock' for track '18' (RT) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
> - Validation warning: Action 'Action_PullBlock' for track '21' (LG) duration 96 frames exceeds threshold 90 frames [start=25, end=120].
> - Action 'Action_PullLeadBlock' range [25-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [93-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [101-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 121, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [121-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [37-39] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [49-55] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [73-92] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [106-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-227] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-118] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-124] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-160] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-189] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [72-193] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [197-211] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [229-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-94] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [25-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [80-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [102-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [25-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [112-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-219] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-185] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [169-179] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-231] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '30' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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