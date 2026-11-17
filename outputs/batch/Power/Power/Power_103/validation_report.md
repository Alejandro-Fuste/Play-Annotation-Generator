# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_103`
- **Input XML**: `outputs/batch/Power/Power/Power_103/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 208: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '2' (C) duration 113 frames exceeds threshold 90 frames [start=127, end=239].
> - Validation warning: Action 'Action_PullBlock' for track '6' (LG) duration 113 frames exceeds threshold 90 frames [start=127, end=239].
> - Validation warning: Action 'Action_DownBlock' for track '21' (RT) duration 113 frames exceeds threshold 90 frames [start=127, end=239].
> - Action 'Action_DownBlock' range [127-172] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [177-194] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-233] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-236] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-233] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-200] for track '24' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.