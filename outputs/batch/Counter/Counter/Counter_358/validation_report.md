# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_358`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_358/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '1' (RG) duration 106 frames exceeds threshold 90 frames [start=187, end=292].
> - Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [184–203], lower_priority='Action_DownBlock' annotated_start=187, effective_Action_DownBlock_start=204.
> - Segment 'Action_DownBlock' for track '14' has invalid range: start=187, end=183. Clamping end to start.
> - Action 'Action_None' range [184-348] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-350] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-225] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [253-280] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [184-199] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [207-223] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [225-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [282-283] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [299-445] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [187-262] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [265-267] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-228] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-249] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-258] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-238] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-263] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-379] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-288] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-230] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-260] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-366] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-267] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-194] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-240] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-278] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-393] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-238] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-293] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-347] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-391] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-280] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-409] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-293] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-395] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-347] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-455] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-390] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-354] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-341] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [348-419] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-399] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-383] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-449] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-458] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.