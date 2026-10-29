# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_27`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [8–24], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=25.
> - Action 'Action_None' range [8-110] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-182] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-231] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-174] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-183] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-45] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [24-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-198] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [177-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [188-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [134-163] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [202-216] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [226-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [236-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [129-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [177-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [188-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [202-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [222-235] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-83] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-106] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-174] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-211] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-196] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-212] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.