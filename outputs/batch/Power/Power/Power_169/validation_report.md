# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_169`
- **Input XML**: `outputs/batch/Power/Power/Power_169/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 340: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [27-392] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-419] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-397] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-418] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-412] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-313] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-340] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-348] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-337] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-344] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-310] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-318] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-343] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-353] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-415] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [247-264] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-302] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-334] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-307] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-419] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-305] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-419] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-348] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-363] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-359] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-399] for track '24' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.