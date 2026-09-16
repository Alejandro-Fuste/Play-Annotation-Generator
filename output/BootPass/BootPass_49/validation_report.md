# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_49`
- **Input XML**: `output/BootPass/BootPass_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 19 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 50 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '1' has invalid range: start=235, end=215. Clamping end to start.
> - Action 'Action_PreSnap' range [19-96] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-179] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-169] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-227] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-195] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-207] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-176] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-199] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-214] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-130] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-143] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-195] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-202] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-197] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-22] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-213] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-115] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-208] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-205] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-237] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-225] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-232] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-237] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.