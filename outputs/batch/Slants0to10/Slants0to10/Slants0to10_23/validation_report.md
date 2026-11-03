# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_23`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 23: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_PassBlock' for track '15' has invalid range: start=17, end=8. Clamping end to start.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [9–23], lower_priority='Action_PassBlock' annotated_start=17, effective_Action_PassBlock_start=24.
> - Action 'Action_None' range [9-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-85] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [88-122] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-139] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-194] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-86] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-171] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-167] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-137] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-62] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [9-18] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [33-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [90-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-46] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-168] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-206] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '30' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.