# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_209`
- **Input XML**: `outputs/batch/Power/Power/Power_209/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [17-263] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-347] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [240-252] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-307] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-289] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-352] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [240-246] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [248-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [251-283] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [285-296] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-355] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-359] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [240-295] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [298-309] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-329] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-339] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-20] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-359] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-316] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-343] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-336] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-359] for track '25' has 1 frames without a visible bounding box.
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