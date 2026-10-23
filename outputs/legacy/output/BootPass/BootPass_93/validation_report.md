# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_93`
- **Input XML**: `output/BootPass/BootPass_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 101 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-185] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-222] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-214] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-236] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [223-232] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [234-236] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-257] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-245] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-219] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-237] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-268] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-259] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-269] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-249] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.