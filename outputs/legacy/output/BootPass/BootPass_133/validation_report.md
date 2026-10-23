# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_133`
- **Input XML**: `output/BootPass/BootPass_133/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 146 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 50 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-36] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-176] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-191] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-209] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-56] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-61] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-201] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-137] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-144] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-162] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-97] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-110] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-163] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-40] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-32] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-78] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-85] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [96-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [111-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [76-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [85-91] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-33] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-67] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunFlatRoute' range [91-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunFlatRoute' range [102-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [113-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-191] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-32] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-56] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-33] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-25] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-111] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-137] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-22] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-68] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-210] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-84] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-110] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-189] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-80] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-86] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-113] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-194] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-85] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-101] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-110] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-201] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-123] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-139] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-115] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-111] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-124] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-177] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-164] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-182] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-210] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-174] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-181] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-210] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-187] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-198] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '37' has 1 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.