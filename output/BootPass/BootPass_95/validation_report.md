# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_95`
- **Input XML**: `output/BootPass/BootPass_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 16 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-205] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-232] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-172] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-179] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-204] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-242] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-265] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [81-85] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-269] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-75] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-105] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-112] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-149] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-115] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-77] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-92] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-103] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-173] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-97] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-132] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-168] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-150] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-220] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-211] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-223] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-227] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-231] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-245] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-247] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-260] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-268] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-269] for track '38' has 1 frames without a visible bounding box.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.