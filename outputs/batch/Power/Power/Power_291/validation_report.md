# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_291`
- **Input XML**: `outputs/batch/Power/Power/Power_291/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 582: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 582: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - Row 582: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [17-252] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-377] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-236] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-380] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-335] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-343] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-334] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-234] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-326] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-386] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-252] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [188-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [215-216] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-364] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-237] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-254] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [188-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-266] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-249] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-262] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-276] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-389] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-340] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-362] for track '29' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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