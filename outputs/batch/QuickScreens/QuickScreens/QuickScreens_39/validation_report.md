# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_39`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Overlapping action conflict at frame 14 for track '7': 'Action_ScreenBlock' vs 'Action_SnapReceive'. Overriding with 'Action_SnapReceive'.
> - Action 'Action_None' range [1-68] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-68] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-68] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-68] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-22] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-16] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-14] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-32] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-16] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [66-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-47] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-11] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-28] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-68] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [1-14] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-20] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-10] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-68] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-8] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-68] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-47] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-68] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-57] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.