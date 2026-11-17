# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_129`
- **Input XML**: `outputs/batch/Power/Power/Power_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [9-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-267] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-276] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-283] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-290] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-274] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-292] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-241] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [169-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-187] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-252] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-237] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [169-211] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [214-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-271] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-276] for track '22' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.