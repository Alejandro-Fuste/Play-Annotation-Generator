# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_35`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 50: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [14–30], lower_priority='Action_PassBlock' annotated_start=17, effective_Action_PassBlock_start=31.
> - Action 'Action_None' range [14-153] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-248] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-101] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-114] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-128] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [125-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [30-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SellStop' range [54-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-158] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-158] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-71] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [14-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-166] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-103] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-142] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-143] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-152] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-170] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-159] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-166] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-264] for track '32' has 3 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.