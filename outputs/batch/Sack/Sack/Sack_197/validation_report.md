# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_197`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_197/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 199, Column 'Wrap Quarterback': Unknown actor track ID '?' in entry '108,?'.
> - Row 199, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '119,?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 396: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-73] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [97-132] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-114] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-55] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-76] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-86] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-106] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '18' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.