# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_102`
- **Input XML**: `output/BootPass/BootPass_102/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 112 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-73] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-195] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-273] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-325] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-208] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-186] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-192] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-306] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-319] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-197] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-294] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-292] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-310] for track '31' has 2 frames without a visible bounding box.
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