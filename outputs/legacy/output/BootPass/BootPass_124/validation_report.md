# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_124`
- **Input XML**: `output/BootPass/BootPass_124/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 79 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '8' has invalid range: start=197, end=126. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '16' has invalid range: start=174, end=118. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '20' has invalid range: start=118, end=79. Clamping end to start.
> - Action 'Action_PreSnap' range [0-245] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-281] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-301] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-310] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-320] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-112] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-346] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-148] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-161] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-287] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-271] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-233] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-245] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-343] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-358] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BootAway' range [118-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [154-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [166-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-358] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-319] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-330] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-301] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-331] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-230] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-271] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-274] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-281] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-325] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-328] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-250] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-257] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-265] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-283] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-317] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-321] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-326] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-355] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-355] for track '36' has 2 frames without a visible bounding box.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.