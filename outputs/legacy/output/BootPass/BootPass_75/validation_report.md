# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_75`
- **Input XML**: `output/BootPass/BootPass_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 59 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [185-197] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-236] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-186] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-192] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-230] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-208] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-94] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-186] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-216] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-220] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-224] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-223] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-239] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-239] for track '33' has 1 frames without a visible bounding box.
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