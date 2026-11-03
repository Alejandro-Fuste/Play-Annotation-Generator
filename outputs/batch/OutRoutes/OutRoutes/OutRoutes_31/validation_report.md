# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_31`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 38: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-229] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-111] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-93] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-229] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-78] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-119] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [232-233] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-149] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-187] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-187] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-200] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-237] for track '30' has 1 frames without a visible bounding box.
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