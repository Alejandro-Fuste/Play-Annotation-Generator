# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_94`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_94/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-86] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [63-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-125] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-221] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-234] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-89] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-111] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-191] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-120] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-217] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-220] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-291] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-113] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-274] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-319] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-153] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-264] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-205] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-274] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-213] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-219] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-228] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-329] for track '29' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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