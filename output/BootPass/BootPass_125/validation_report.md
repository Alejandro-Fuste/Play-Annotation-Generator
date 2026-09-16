# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_125`
- **Input XML**: `output/BootPass/BootPass_125/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 64 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '4' has invalid range: start=308, end=299. Clamping end to start.
> - Action 'Action_PreSnap' range [0-277] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-278] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-288] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-294] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [98-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-294] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-276] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-160] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-266] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-281] for track '28' has 1 frames without a visible bounding box.
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
> - Action event 'Action_SecureCatch' has invalid start frame 308. Video range is [0, 299].

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.