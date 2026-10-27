# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_41`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '17' (C) duration 107 frames exceeds threshold 90 frames [start=129, end=235].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [126–143], lower_priority='Action_DownBlock' annotated_start=129, effective_Action_DownBlock_start=144.
> - Validation warning: Action 'Action_PullBlock' for track '20' (LG) duration 107 frames exceeds threshold 90 frames [start=129, end=235].
> - Action 'Action_None' range [126-265] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [174-273] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [129-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [211-235] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-287] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-277] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-246] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-264] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-279] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [171-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [185-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-208] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-259] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-288] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-294] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-270] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-281] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-203] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [153-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-179] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-189] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-185] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-265] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-252] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-299] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '27' has 1 frames without a visible bounding box.
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