# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_120`
- **Input XML**: `output/BootPass/BootPass_120/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 40 |
| Ball Tracks | 1 |
| CSV events parsed | 6 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 61 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '2' has invalid range: start=172, end=124. Clamping end to start.
> - Action 'Action_PreSnap' range [0-147] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-92] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-73] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-102] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-113] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [93-128] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 134, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [134-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 146, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [146-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-75] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-92] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-139] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-139] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-163] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-242] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-160] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-268] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-267] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-263] for track '39' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.