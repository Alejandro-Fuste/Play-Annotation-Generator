# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_39`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

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
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 54: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [5–9], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=10.
> - Action 'Action_RunGoRoute' range [77-195] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [199-205] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-54] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-219] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-217] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-44] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-81] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-48] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-266] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-224] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-237] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [170-180] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [182-189] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [195-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [201-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [175-189] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [130-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [135-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [152-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [156-212] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-218] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-166] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-228] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-237] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-259] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '30' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.