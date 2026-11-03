# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_49`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 53: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [53-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [69-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-49] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-60] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-90] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-85] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [14-45] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-90] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-90] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [14-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-49] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-90] for track '21' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.