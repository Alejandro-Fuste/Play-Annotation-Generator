# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_6`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [13–28], lower_priority='Action_PassBlock' annotated_start=16, effective_Action_PassBlock_start=29.
> - Action 'Action_None' range [13-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-62] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-39] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [123-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SellOut' range [63-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [112-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-65] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-158] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [59-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-130] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-191] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '29' has 1 frames without a visible bounding box.
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