# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_60`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 39 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 122: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [92-95] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [97-104] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [115-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-99] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-86] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-56] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-120] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [92-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [96-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [100-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-120] for track '19' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.