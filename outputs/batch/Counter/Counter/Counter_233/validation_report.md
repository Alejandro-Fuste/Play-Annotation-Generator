# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_233`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_233/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 468: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 468: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '12' (RT) duration 143 frames exceeds threshold 90 frames [start=247, end=389].
> - Validation warning: Action 'Action_PullBlock' for track '16' (RG) duration 143 frames exceeds threshold 90 frames [start=247, end=389].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [245–263], lower_priority='Action_DownBlock' annotated_start=247, effective_Action_DownBlock_start=264.
> - Validation warning: Action 'Action_DownBlock' for track '21' (LG) duration 143 frames exceeds threshold 90 frames [start=247, end=389].
> - Action 'Action_None' range [245-346] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-353] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [247-341] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [345-347] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-297] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-375] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [377-387] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-390] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-419] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-419] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-348] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-309] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-419] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [247-389] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [390-419] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-373] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-403] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-317] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-325] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-350] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [247-326] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [332-336] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [264-280] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-287] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-330] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-335] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-348] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [247-263] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [267-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [279-301] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [307-333] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [391-392] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-381] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [387-409] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-419] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-304] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-383] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-385] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-382] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-388] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-417] for track '29' has 2 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.