# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_90`
- **Input XML**: `output/BootPass/BootPass_90/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 21 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-75] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-215] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-151] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-80] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-145] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-49] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-147] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-156] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-75] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-134] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-118] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-247] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-125] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-139] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-141] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-156] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-153] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-267] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-258] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-204] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-244] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-249] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-259] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-237] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-247] for track '35' has 1 frames without a visible bounding box.
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