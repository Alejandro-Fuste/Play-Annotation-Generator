# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_44`
- **Input XML**: `output/BootPass/BootPass_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 25 |
| Ball Tracks | 1 |
| CSV events parsed | 6 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 53 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-116] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-160] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-88] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-162] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-168] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-153] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [184-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-197] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-210] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.