# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_42`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_42/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 52: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [7–23], lower_priority='Action_PassBlock' annotated_start=10, effective_Action_PassBlock_start=24.
> - Action 'Action_None' range [7-191] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-17] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-156] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [119-138] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [7-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-188] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-176] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-200] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [7-57] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-144] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-51] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-84] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-30] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-36] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-184] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-17] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-188] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [52-63] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-82] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-117] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-197] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-188] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-193] for track '28' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.