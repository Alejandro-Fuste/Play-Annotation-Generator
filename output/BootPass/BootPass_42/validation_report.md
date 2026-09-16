# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_42`
- **Input XML**: `output/BootPass/BootPass_42/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 62 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-239] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-239] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-176] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-236] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-212] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-231] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-170] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-181] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-149] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-194] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-198] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.