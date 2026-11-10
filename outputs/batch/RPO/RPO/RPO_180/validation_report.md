# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_180`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_180/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 40 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['LG', 'LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 330: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-114] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-88] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-110] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PullBall' range [56-67] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-72] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-114] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-23] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-72] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-110] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-150] for track '20' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.