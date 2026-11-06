# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_90`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_90/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [0-203] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-384] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_Keep' range [102-207] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [209-241] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-389] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-242] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-372] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-379] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-389] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-231] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-386] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-88] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-354] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-389] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-279] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-366] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.