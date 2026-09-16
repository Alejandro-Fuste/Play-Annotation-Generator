# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_76`
- **Input XML**: `output/BootPass/BootPass_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 6 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 35 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [161-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [67-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-149] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-103] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-210] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.