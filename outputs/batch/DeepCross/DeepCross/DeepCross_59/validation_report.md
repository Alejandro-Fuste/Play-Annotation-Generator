# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_59`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 62: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 62: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 62: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_ThrowPass' for track '7' has invalid range: start=127, end=54. Clamping end to start.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [16–31], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=32.
> - Action 'Action_None' range [16-197] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-223] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [31-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [204-221] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-100] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-201] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-83] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-49] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-54] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-244] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-81] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [98-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-140] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-192] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-246] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-261] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-231] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-251] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [253-265] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-203] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-236] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-223] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [230-246] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [253-261] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-194] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [197-202] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-218] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [191-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [197-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [203-215] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-52] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [131-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-122] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-209] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-232] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-263] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-235] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-244] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-232] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-251] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-265] for track '31' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.