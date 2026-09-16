# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_67`
- **Input XML**: `output/BootPass/BootPass_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 5 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 15 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 27 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_BootAway' for track '15' has invalid range: start=50, end=44. Clamping end to start.
> - Segment 'Action_RunFlatRoute' for track '15' has invalid range: start=78, end=44. Clamping end to start.
> - Action 'Action_PreSnap' range [14-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-71] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-232] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-79] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-169] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-187] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-203] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-219] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-278] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-289] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-348] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-363] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-248] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-82] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-234] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-306] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-242] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-388] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-225] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-215] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-291] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-53] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-378] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-383] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-388] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-324] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-152] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-162] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-170] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-186] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-213] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-238] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-283] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-222] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-349] for track '33' has 1 frames without a visible bounding box.
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