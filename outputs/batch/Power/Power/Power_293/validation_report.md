# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_293`
- **Input XML**: `outputs/batch/Power/Power/Power_293/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 586: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [22-329] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-274] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-306] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-317] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-322] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-74] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-89] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-249] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-272] for track '29' has 2 frames without a visible bounding box.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.