# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_126`
- **Input XML**: `output/BootPass/BootPass_126/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 185 could not be resolved to any XML tracks (position/team_side missing).
> - Event 'Action_SecureCatch' at frame 245 targets track ID '37', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_FakeHandoff' for track '2' has invalid range: start=175, end=132. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '2' has invalid range: start=192, end=132. Clamping end to start.
> - Segment 'Action_BootAway' for track '2' has invalid range: start=214, end=132. Clamping end to start.
> - Action 'Action_PreSnap' range [0-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-217] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-234] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-187] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-269] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-259] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-214] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-255] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '33' has 1 frames without a visible bounding box.
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