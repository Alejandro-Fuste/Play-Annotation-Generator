# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_36`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
> - Action 'Action_None' range [209-320] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-380] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-378] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-389] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-340] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-375] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-292] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-323] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-316] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-324] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-344] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-358] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-374] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [210-284] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-372] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [210-282] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [284-286] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-368] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-375] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-360] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-375] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-163] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-208] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-216] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-378] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-287] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-295] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-337] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-316] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-331] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-338] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-383] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-344] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-387] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-356] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-386] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-387] for track '30' has 1 frames without a visible bounding box.
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