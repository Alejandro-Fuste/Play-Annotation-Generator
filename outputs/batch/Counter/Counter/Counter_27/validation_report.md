# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_27`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [121–139], lower_priority='Action_DownBlock' annotated_start=134, effective_Action_DownBlock_start=140.
> - Action 'Action_None' range [121-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-329] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-197] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-271] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-315] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [184-328] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [134-158] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-302] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-291] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-328] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-217] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-227] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-329] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [121-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-246] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-283] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.