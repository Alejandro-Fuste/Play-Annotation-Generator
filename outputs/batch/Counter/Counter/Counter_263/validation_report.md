# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_263`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_263/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 528: Duplicate assignment for track ID '22' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_DownBlock' for track '18' has invalid range: start=54, end=50. Clamping end to start.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [51–66], lower_priority='Action_DownBlock' annotated_start=54, effective_Action_DownBlock_start=67.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [51–66], lower_priority='Action_SnapReceive' annotated_start=51, effective_Action_SnapReceive_start=67.
> - Action 'Action_None' range [51-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [54-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [114-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-143] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [54-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-159] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [54-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [51-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '18' starts at frame 95, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [95-150] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [54-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-192] for track '24' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.