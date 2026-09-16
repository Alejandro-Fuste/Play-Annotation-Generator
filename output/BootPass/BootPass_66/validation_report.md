# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_66`
- **Input XML**: `output/BootPass/BootPass_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 67 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-231] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-269] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-236] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-152] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-91] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-230] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-157] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-265] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-260] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-243] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-247] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-259] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-263] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.