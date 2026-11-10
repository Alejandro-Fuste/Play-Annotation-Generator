# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_85`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 156: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [30-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-59] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-114] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-134] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [40-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [56-62] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-65] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-64] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-53] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-129] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '26' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.