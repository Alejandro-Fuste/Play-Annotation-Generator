# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_119`
- **Input XML**: `output/BootPass/BootPass_119/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 5 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 56 could not be resolved to any XML tracks (position/team_side missing).
> - Event 'Action_SecureCatch' at frame 171 targets track ID '39', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_ThrowPass' for track '20' has invalid range: start=148, end=109. Clamping end to start.
> - Action 'Action_PreSnap' range [0-182] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-209] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-263] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-227] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-254] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-249] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-188] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-109] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-190] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-198] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-216] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-246] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-255] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-247] for track '26' has 1 frames without a visible bounding box.
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