# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_374`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_374/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [5–19], lower_priority='Action_ZoneBlock' annotated_start=8, effective_Action_ZoneBlock_start=20.
> - Action 'Action_None' range [5-50] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-254] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-18] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-44] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-96] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-50] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-315] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-33] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-47] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-211] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-261] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-312] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-316] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.