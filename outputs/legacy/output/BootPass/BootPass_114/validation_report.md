# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_114`
- **Input XML**: `output/BootPass/BootPass_114/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 63 could not be resolved to any XML tracks (position/team_side missing).
> - Event 'Action_RunFlatRoute' at frame 21 targets track ID 'Drag', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_ThrowPass' for track '4' has invalid range: start=145, end=114. Clamping end to start.
> - Segment 'Action_SecureCatch' for track '25' has invalid range: start=194, end=112. Clamping end to start.
> - Action 'Action_PreSnap' range [0-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-149] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-284] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-290] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [97-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-249] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-250] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-278] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-201] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-299] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '20' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-153] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-166] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-103] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-235] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-279] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-225] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-290] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-294] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-285] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.