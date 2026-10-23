# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_23`
- **Input XML**: `output/BootPass/BootPass_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 47 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-241] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-260] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-235] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-247] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-260] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-92] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-157] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-224] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-249] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-194] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-269] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.