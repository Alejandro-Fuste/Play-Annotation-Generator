# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_188`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_188/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [40-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-86] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-57] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-106] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-173] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-250] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-254] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-109] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-112] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-226] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-211] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-248] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-245] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-253] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-231] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-250] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-251] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-256] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-251] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-243] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '33' has 2 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.