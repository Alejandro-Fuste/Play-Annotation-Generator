# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_365`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_365/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 732: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 732: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 94 frames exceeds threshold 90 frames [start=219, end=312].
> - Validation warning: Action 'Action_PullBlock' for track '9' (LG) duration 94 frames exceeds threshold 90 frames [start=219, end=312].
> - Validation warning: Action 'Action_DownBlock' for track '15' (RT) duration 94 frames exceeds threshold 90 frames [start=219, end=312].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [216–230], lower_priority='Action_DownBlock' annotated_start=219, effective_Action_DownBlock_start=231.
> - Action 'Action_None' range [216-324] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-356] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-337] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-353] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-355] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-275] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-286] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-328] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [219-267] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [269-312] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-336] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-358] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-320] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-344] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-357] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-263] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [219-271] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [274-312] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-331] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [333-351] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-334] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [231-265] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [274-275] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-240] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-341] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [343-357] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-24] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-89] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-61] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-303] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-321] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-341] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-346] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-301] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-352] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-355] for track '33' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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