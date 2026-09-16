# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_87`
- **Input XML**: `output/BootPass/BootPass_87/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
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
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 43 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-212] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-224] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-240] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-248] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-257] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-190] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-84] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-247] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-265] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-224] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-247] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.