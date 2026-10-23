# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_11`
- **Input XML**: `output/BootPass/BootPass_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 120 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-224] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-298] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-236] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-299] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-279] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-286] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-28] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-65] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-160] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-299] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-205] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-270] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-289] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '27' has 1 frames without a visible bounding box.
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