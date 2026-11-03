# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_87`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_87/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 92: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [12-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-46] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-99] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [74-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-102] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-101] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-120] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-120] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [12-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-26] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-37] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-74] for track '23' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.