# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_259`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_259/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 520: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '13' (LT) duration 100 frames exceeds threshold 90 frames [start=81, end=180].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [78–92], lower_priority='Action_DownBlock' annotated_start=81, effective_Action_DownBlock_start=93.
> - Validation warning: Action 'Action_PullBlock' for track '19' (RG) duration 100 frames exceeds threshold 90 frames [start=81, end=180].
> - Action 'Action_None' range [78-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-229] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-257] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-266] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-252] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [123-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [218-229] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-229] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-251] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-188] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-231] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-236] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-258] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-114] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-240] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [81-96] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [124-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-228] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-254] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-267] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-226] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-168] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-248] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [93-96] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [98-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [81-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [93-137] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [157-170] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [81-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [90-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-218] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-257] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-228] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-252] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-117] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-218] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-267] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '28' has 1 frames without a visible bounding box.
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