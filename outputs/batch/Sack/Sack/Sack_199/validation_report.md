# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_199`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_199/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 8 |
| Action Segments inferred | 41 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 400: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-78] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [99-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-14] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-23] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-42] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-28] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-78] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [90-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [101-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-117] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '21' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.