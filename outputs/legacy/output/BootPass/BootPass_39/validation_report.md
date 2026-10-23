# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_39`
- **Input XML**: `output/BootPass/BootPass_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 68 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-252] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-215] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-238] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-258] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-269] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-215] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '14' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-124] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-234] for track '16' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-124] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-269] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-258] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-202] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-235] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-249] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-193] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-269] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-213] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-259] for track '29' has 1 frames without a visible bounding box.
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