# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_8`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [34-102] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-103] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-59] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-69] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-109] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-51] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-105] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-54] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-62] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-104] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-73] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-86] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-93] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-122] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.