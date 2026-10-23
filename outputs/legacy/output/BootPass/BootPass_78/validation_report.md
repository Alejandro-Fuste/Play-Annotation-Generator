# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_78`
- **Input XML**: `output/BootPass/BootPass_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 30 |
| Ball Tracks | 1 |
| CSV events parsed | 7 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 63 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-93] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-157] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-166] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-138] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-90] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-129] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-269] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-88] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-152] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-238] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-267] for track '30' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.