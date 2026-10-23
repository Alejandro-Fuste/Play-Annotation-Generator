# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_97`
- **Input XML**: `output/BootPass/BootPass_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 120 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-250] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-288] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-296] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-312] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [202-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-226] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [128-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-218] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-223] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-234] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-223] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-272] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-299] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-312] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-321] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-307] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-315] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-321] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-326] for track '29' has 1 frames without a visible bounding box.
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