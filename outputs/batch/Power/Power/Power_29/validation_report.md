# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_29`
- **Input XML**: `outputs/batch/Power/Power/Power_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 43 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 60: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [22-352] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-362] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-307] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-389] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-369] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-389] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-322] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-352] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-375] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-389] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-286] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-300] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-321] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-332] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-338] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-361] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-387] for track '28' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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