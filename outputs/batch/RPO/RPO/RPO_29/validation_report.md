# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_29`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 24 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [119-123] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-142] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-188] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-195] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-111] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-226] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [132-192] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-239] for track '24' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.