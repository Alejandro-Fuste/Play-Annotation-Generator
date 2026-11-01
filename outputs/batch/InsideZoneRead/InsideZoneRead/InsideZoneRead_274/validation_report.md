# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_274`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_274/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 548: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 548: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [15-52] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-215] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-82] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-41] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [64-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-88] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-37] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [40-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-35] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [30-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-20] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-37] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-26] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-40] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.