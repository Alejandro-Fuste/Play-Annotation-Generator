# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_85`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 88: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 88: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 88: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 88: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 88: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ThrowPass' for track '16' has invalid range: start=120, end=43. Clamping end to start.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [2–6], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=7.
> - Action 'Action_None' range [2-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-210] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [16-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-198] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-58] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-198] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-50] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-24] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-106] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-195] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [2-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-179] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-199] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-43] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-13] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-110] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-10] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-106] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-10] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-15] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-48] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-187] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-192] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [37-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-172] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-188] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-159] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-169] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-186] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-206] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '32' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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