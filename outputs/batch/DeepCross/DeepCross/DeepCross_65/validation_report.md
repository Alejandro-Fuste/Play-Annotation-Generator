# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_65`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 68: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 68: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [13–28], lower_priority='Action_PassBlock' annotated_start=16, effective_Action_PassBlock_start=29.
> - Action 'Action_None' range [13-206] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [30-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-55] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-239] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [13-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-177] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-207] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [209-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [215-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-183] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [188-194] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [196-225] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [227-228] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-234] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-167] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-231] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-26] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-74] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-80] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-48] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-76] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-130] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-148] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-230] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-237] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-223] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-232] for track '29' has 2 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.