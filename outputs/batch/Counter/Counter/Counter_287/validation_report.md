# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_287`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_287/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 576: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '11' (RG) duration 93 frames exceeds threshold 90 frames [start=148, end=240].
> - Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 93 frames exceeds threshold 90 frames [start=148, end=240].
> - Validation warning: Action 'Action_DownBlock' for track '21' (LT) duration 93 frames exceeds threshold 90 frames [start=148, end=240].
> - Action 'Action_None' range [145-245] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-340] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-241] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-245] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-321] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-226] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [148-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-323] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-267] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-298] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-257] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-286] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-358] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [148-240] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-359] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-245] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [174-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [187-240] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-345] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-359] for track '25' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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