# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_63`
- **Input XML**: `outputs/batch/Power/Power/Power_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 128: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [8-296] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-330] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-262] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-294] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-292] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-337] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-282] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-266] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-315] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [219-220] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [248-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [219-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [263-267] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-359] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-337] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-345] for track '27' has 2 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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