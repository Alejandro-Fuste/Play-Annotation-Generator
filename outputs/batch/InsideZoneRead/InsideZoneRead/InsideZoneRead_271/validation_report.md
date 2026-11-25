# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_271`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_271/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [18-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-149] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-74] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-61] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [62-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [114-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [40-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-50] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-72] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [75-111] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-180] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-180] for track '30' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_271'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.