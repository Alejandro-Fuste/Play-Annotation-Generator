# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_265`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_265/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [79–93], lower_priority='Action_DownBlock' annotated_start=82, effective_Action_DownBlock_start=94.
> - Action 'Action_DownBlock' range [82-102] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [104-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-211] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-269] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-269] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-197] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [82-131] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-251] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-240] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [79-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-237] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [82-84] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-266] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-261] for track '28' has 1 frames without a visible bounding box.
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