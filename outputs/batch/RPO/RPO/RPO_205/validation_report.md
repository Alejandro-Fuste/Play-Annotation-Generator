# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_205`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_205/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [46-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [94-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [47-103] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-60] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [62-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-150] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-150] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '28' has 1 frames without a visible bounding box.
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