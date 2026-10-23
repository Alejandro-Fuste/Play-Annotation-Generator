# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_116`
- **Input XML**: `output/BootPass/BootPass_116/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 56 |
| Player Tracks | 55 |
| Ball Tracks | 1 |
| CSV events parsed | 6 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 50 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SnapReceive' for track '19' has invalid range: start=134, end=50. Clamping end to start.
> - Segment 'Action_BootAway' for track '19' has invalid range: start=134, end=86. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '19' has invalid range: start=134, end=107. Clamping end to start.
> - Action 'Action_PreSnap' range [0-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-267] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-252] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-203] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-232] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-193] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [121-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-229] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-189] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-220] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-146] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-200] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-242] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-213] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-191] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-193] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-191] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-195] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-215] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-215] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-193] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-267] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-205] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-197] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-197] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-230] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-226] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-211] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-215] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-236] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-246] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-218] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-232] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-220] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-224] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-269] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-246] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-269] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-248] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-266] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-264] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '55' has 1 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.