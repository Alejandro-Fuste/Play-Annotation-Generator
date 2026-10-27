# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_389`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_389/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 780: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 780: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '9' (C) duration 109 frames exceeds threshold 90 frames [start=144, end=252].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [141–156], lower_priority='Action_DownBlock' annotated_start=144, effective_Action_DownBlock_start=157.
> - Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 109 frames exceeds threshold 90 frames [start=144, end=252].
> - Action 'Action_None' range [141-389] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-310] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-233] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-272] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-348] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-389] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [144-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-274] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-389] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [144-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [206-209] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-377] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [382-389] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-166] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-389] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-252] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-266] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-274] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-261] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-330] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [334-364] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-376] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-380] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-294] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [301-389] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-307] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-330] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-336] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-344] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '33' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.