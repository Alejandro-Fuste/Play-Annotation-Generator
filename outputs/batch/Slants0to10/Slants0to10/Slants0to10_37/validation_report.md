# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Slants0to10_37`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 20, Column 'Pass Block': Could not parse frame number from '-' in entry '-,OL'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 38: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - Row 38: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Overlapping action conflict at frame 12 for track '16': 'Action_SnapReceive' vs 'Action_RunSlantRoute'. Overriding with 'Action_RunSlantRoute'.
> - Segment 'Action_BallCarry' for track '16' has invalid range: start=89, end=71. Clamping end to start.
> - Action 'Action_PreSnap' range [0-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [49-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-195] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-239] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-105] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-239] for track '29' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.