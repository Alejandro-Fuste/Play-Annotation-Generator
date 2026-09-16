# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_100`
- **Input XML**: `output/BootPass/BootPass_100/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 62 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '17' has invalid range: start=294, end=239. Clamping end to start.
> - Action 'Action_PreSnap' range [0-206] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-215] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-197] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-211] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-153] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [81-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [100-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-134] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-166] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-159] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-151] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-160] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-151] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '33' has 1 frames without a visible bounding box.
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
> - Action event 'Action_SecureCatch' has invalid start frame 294. Video range is [0, 239].

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.