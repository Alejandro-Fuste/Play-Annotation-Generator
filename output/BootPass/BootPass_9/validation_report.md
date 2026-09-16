# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_9`
- **Input XML**: `output/BootPass/BootPass_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 37 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-204] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-212] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-285] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-241] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-216] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-226] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-257] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-287] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-123] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-172] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-189] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-240] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-261] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-282] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-193] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-254] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-288] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-286] for track '30' has 1 frames without a visible bounding box.
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