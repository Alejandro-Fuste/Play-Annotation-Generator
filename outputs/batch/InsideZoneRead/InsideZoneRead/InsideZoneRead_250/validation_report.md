# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_250`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_250/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [13–29], lower_priority='Action_ZoneBlock' annotated_start=16, effective_Action_ZoneBlock_start=30.
> - Action 'Action_None' range [13-68] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-57] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-88] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-103] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-54] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-110] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-35] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-32] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-107] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-147] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-49] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-95] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-111] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-44] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [25-98] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-196] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-87] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-228] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.