# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_17`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 30: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [5–19], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=20.
> - Action 'Action_None' range [5-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-40] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-89] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-143] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-257] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [93-193] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-165] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-168] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-233] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '28' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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