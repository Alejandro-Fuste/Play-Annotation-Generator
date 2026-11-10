# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_88`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 8 |
| Action Segments inferred | 36 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 90, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '120,134;?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 178: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-126] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [100-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-100] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-133] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-72] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-118] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [110-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [132-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-150] for track '19' has 1 frames without a visible bounding box.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.