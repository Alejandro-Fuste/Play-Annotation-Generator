# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_98`
- **Input XML**: `output/BootPass/BootPass_98/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 24 |
| Ball Tracks | 1 |
| CSV events parsed | 7 |
| Action Segments inferred | 39 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 111 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' for track '10' starts at frame 184, but the player has no visible bounding box on this frame.
> - Action 'Action_SecureCatch' range [184-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [122-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-201] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-230] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-299] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-295] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-291] for track '21' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.