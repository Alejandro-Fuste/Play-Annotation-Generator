# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_368`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_368/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '11' (RG) duration 127 frames exceeds threshold 90 frames [start=45, end=171].
> - Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 111 frames exceeds threshold 90 frames [start=45, end=155].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [42–56], lower_priority='Action_DownBlock' annotated_start=45, effective_Action_DownBlock_start=57.
> - Validation warning: Action 'Action_DownBlock' for track '14' (LT) duration 168 frames exceeds threshold 90 frames [start=45, end=212].
> - Action 'Action_None' range [42-280] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [42-281] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-230] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-241] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [86-177] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [180-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-176] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-191] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-276] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-299] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-193] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-241] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-253] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-281] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-262] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [45-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [45-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [184-204] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [57-155] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [45-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [211-212] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-215] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-271] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-291] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-212] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-224] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-247] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-293] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.