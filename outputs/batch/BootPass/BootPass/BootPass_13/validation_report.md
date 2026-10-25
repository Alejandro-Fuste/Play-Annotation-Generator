# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_13`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 28: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [25–41], lower_priority='Action_RunBlock' annotated_start=33, effective_Action_RunBlock_start=42.
> - Action 'Action_None' range [142-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-158] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-54] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-69] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-45] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-54] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-178] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-135] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [33-88] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [48-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [33-133] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [136-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [142-161] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [169-181] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [206-227] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [230-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-229] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [25-34] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [72-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [33-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [80-93] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [101-129] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [134-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [137-182] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [33-52] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-16] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-188] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-239] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-152] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-163] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-227] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [146-212] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-235] for track '30' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.