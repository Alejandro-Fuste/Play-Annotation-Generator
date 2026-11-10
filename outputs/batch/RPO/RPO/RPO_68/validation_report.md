# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_68`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_68/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 64, Column 'Route': Invalid or unassigned actor track ID '-' in Route descriptor 'Out,-'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [67-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-118] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-123] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-86] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-123] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-125] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-109] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-231] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-238] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-248] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-268] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-248] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [242-256] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-269] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [260-266] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.