# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_1`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [20–36], lower_priority='Action_PassBlock' annotated_start=23, effective_Action_PassBlock_start=37.
> - Action 'Action_None' range [20-269] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [20-56] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-198] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-234] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [20-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-199] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-189] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-243] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [91-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [108-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-154] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-211] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-222] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-149] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-160] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-252] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [260-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [205-260] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-269] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-196] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-228] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-250] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-254] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '32' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.