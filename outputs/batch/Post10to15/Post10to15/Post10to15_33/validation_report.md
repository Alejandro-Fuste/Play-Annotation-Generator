# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_33`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [1–14], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=15.
> - Action 'Action_None' range [1-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-80] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [14-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [109-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-113] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-108] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-193] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-182] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-209] for track '28' has 1 frames without a visible bounding box.
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