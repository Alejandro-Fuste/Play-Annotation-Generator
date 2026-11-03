# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_29`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
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
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [19–32], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=33.
> - Action 'Action_None' range [19-137] for track '3' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [19-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-228] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [93-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-115] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-131] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [33-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-165] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.