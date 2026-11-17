# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_205`
- **Input XML**: `outputs/batch/Power/Power/Power_205/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 412: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 412: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [27-300] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-378] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-382] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-261] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-373] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-389] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-300] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-389] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-283] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-316] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-323] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-389] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-366] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-372] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-382] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [245-293] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [245-255] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [263-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [280-286] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-368] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-389] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-389] for track '30' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.