# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_282`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_282/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 565: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '1' (C): higher_priority='Action_BallSnap' [226–241], lower_priority='Action_PullBlock' annotated_start=229, effective_Action_PullBlock_start=242.
> - Action 'Action_None' range [226-276] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [242-254] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-426] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [229-266] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [268-277] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-449] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-300] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-420] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-279] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-283] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 319, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [319-443] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-410] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-417] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-261] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-449] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [229-283] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [286-318] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-449] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [273-288] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-7] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-17] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-322] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-449] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-449] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-449] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-288] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-417] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-422] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-436] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-431] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-354] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-443] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [445-449] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-449] for track '24' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.