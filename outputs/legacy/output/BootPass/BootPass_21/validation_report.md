# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_21`
- **Input XML**: `output/BootPass/BootPass_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 5 |
| Action Segments inferred | 125 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 74 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-242] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-215] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-233] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-218] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-96] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-269] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-110] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-111] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-193] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-84] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-213] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-235] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-245] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-252] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-156] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-267] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-252] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-230] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-235] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-18] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-111] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-185] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-196] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-87] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-140] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-183] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-6] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-79] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-41] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-143] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-156] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-147] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-154] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-231] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-245] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-155] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-177] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-207] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-220] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-235] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-258] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-264] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-261] for track '36' has 1 frames without a visible bounding box.
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