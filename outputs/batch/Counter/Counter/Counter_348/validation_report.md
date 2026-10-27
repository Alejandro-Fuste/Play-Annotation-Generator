# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_348`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_348/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [45–58], lower_priority='Action_PullBlock' annotated_start=48, effective_Action_PullBlock_start=59.
> - Action 'Action_Handoff' range [68-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-173] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [48-73] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [45-195] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-147] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [59-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-171] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-239] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-140] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-239] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '18' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.