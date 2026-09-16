# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_117`
- **Input XML**: `output/BootPass/BootPass_117/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 19 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-220] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-235] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-175] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-171] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-89] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-181] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-157] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '27' has 1 frames without a visible bounding box.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.