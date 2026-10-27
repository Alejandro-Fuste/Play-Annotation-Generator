# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_280`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_280/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 562: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '9' (RG) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
> - Validation warning: Action 'Action_PullBlock' for track '11' (C) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [64–83], lower_priority='Action_PullBlock' annotated_start=67, effective_Action_PullBlock_start=84.
> - Action 'Action_None' range [64-68] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-135] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [67-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [97-109] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-227] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-236] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [114-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [67-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [67-88] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [84-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-233] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-91] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-119] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-236] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-123] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-132] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-35] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-51] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-135] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-179] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '33' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.