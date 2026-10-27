# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_92`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '0' (TE) duration 106 frames exceeds threshold 90 frames [start=76, end=181].
> - Validation warning: Action 'Action_DownBlock' for track '3' (RG) duration 106 frames exceeds threshold 90 frames [start=76, end=181].
> - Validation warning: Action 'Action_PullBlock' for track '6' (LG) duration 106 frames exceeds threshold 90 frames [start=76, end=181].
> - Validation warning: Action 'Action_DownBlock' for track '9' (C) duration 106 frames exceeds threshold 90 frames [start=76, end=181].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [75–93], lower_priority='Action_DownBlock' annotated_start=76, effective_Action_DownBlock_start=94.
> - Action 'Action_DownBlock' range [76-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-258] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-260] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-202] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [86-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [129-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-252] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-96] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-263] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [124-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-252] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-285] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-295] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-346] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-351] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-260] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-274] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-355] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-337] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-347] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-212] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-350] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-292] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-329] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-340] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-350] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-350] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-357] for track '33' has 1 frames without a visible bounding box.
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