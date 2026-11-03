# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_37`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
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
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [10–28], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=29.
> - Action 'Action_RunPostRoute' range [28-123] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [130-134] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [140-142] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [154-159] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [168-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-100] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-113] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-163] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [10-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-144] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [10-13] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [19-24] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [139-171] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [177-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-28] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-122] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [21-143] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-68] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-62] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-145] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-172] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '29' has 1 frames without a visible bounding box.
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