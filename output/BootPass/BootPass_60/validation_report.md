# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_60`
- **Input XML**: `output/BootPass/BootPass_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 57 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-87] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-238] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-95] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-190] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-343] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-389] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-339] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [74-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [85-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' for track '15' starts at frame 88, but the player has no visible bounding box on this frame.
> - Action 'Action_BootAway' range [88-92] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-21] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-60] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-153] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-117] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-113] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-359] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-152] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-310] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-348] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-360] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-389] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-167] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-284] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-296] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-332] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-166] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-222] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-173] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-188] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-177] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-203] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-250] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-348] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-359] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-256] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-265] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-344] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-277] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-290] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-312] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-296] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-380] for track '44' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.