# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_99`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 104: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [10-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [92-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [145-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-48] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [10-48] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-96] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-74] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-74] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-122] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-57] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '24' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.