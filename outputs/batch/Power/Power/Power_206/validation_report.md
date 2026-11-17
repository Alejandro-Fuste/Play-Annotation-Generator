# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_206`
- **Input XML**: `outputs/batch/Power/Power/Power_206/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [13-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-329] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-291] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-300] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-255] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-330] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-310] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [244-283] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-300] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-370] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-296] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [244-272] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-304] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-313] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-337] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [244-250] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-49] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-63] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [244-252] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-313] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-259] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-370] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-378] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-382] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-261] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-271] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-281] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-323] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-308] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-360] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-362] for track '22' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.