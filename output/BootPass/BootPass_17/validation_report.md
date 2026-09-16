# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_17`
- **Input XML**: `output/BootPass/BootPass_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 70 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-263] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-223] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-123] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-255] for track '27' has 1 frames without a visible bounding box.
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