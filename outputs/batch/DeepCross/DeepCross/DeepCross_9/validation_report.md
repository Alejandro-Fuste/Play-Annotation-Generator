# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_9`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 12: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 12: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - Row 12: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [14-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-149] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-151] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-54] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-285] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-50] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-145] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-162] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-231] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-74] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-114] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-144] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.