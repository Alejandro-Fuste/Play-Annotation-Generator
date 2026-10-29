# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_101`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_101/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [23–38], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=39.
> - Action 'Action_BallCarry' range [184-219] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-84] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-134] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-215] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-127] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [134-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-143] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-161] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [163-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [196-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [48-200] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [230-233] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-171] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-189] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-81] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [163-186] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [188-209] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [222-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [162-203] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-133] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-155] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-48] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [147-186] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [190-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [228-237] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-7] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-78] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-159] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-200] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-160] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-206] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-227] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-203] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-237] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.