# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_73`
- **Input XML**: `output/BootPass/BootPass_73/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 54 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-139] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-190] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-116] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-229] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-202] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-213] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-204] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-141] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-107] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-147] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-181] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-190] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-106] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-52] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-146] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-189] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-206] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-228] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-158] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-138] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-221] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-159] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-172] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-194] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-231] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-176] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-239] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '36' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.