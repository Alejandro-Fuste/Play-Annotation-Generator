# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_266`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_266/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '9' (C) duration 92 frames exceeds threshold 90 frames [start=36, end=127].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [33–45], lower_priority='Action_DownBlock' annotated_start=36, effective_Action_DownBlock_start=46.
> - Validation warning: Action 'Action_PullBlock' for track '14' (DT2) duration 92 frames exceeds threshold 90 frames [start=36, end=127].
> - Action 'Action_None' range [33-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-126] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [36-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [86-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [74-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-171] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-65] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [36-124] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [46-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-71] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-186] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-195] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-210] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-119] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-200] for track '24' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.