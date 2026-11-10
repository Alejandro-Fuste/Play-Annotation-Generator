# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_148`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_148/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '11' has invalid range: start=40, end=33. Clamping end to start.
> - Action 'Action_None' range [39-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-104] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-117] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-128] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-161] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-74] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-41] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-49] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-163] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-181] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-262] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.