# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_80`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 89: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 90: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [13–28], lower_priority='Action_PassBlock' annotated_start=16, effective_Action_PassBlock_start=29.
> - Action 'Action_None' range [106-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-145] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-160] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-120] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [135-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-58] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-187] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-43] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-140] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [139-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [143-149] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-64] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-117] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-140] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-176] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-205] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-187] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-179] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '27' has 4 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.