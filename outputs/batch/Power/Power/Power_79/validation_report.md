# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_79`
- **Input XML**: `outputs/batch/Power/Power/Power_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 160: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 160: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '15' (Unknown) duration 92 frames exceeds threshold 90 frames [start=89, end=180].
> - Validation warning: Action 'Action_PullBlock' for track '17' (RG) duration 92 frames exceeds threshold 90 frames [start=89, end=180].
> - Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 92 frames exceeds threshold 90 frames [start=89, end=180].
> - Action 'Action_PreSnap' range [14-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-123] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.