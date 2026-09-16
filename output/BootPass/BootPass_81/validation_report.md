# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_81`
- **Input XML**: `output/BootPass/BootPass_81/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 134 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Overlapping action conflict at frame 157 for track '18': 'Action_FakeHandoff' vs 'Action_BootAway'. Overriding with 'Action_BootAway'.
> - Action 'Action_PreSnap' range [0-289] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-266] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-256] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-262] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-257] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-280] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-244] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-165] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-233] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-264] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-283] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-264] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-253] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-262] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-170] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-185] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-258] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-261] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-261] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-243] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-275] for track '30' has 1 frames without a visible bounding box.
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