# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_59`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [1–17], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=18.
> - Action 'Action_None' range [1-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [87-164] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-55] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-215] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-36] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-103] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [113-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [125-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [131-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-75] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-100] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-128] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-179] for track '26' has 1 frames without a visible bounding box.
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