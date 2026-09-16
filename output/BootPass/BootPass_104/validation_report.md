# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_104`
- **Input XML**: `output/BootPass/BootPass_104/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 38 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [143-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-241] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-250] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-191] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-269] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-203] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-186] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-226] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-242] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-137] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-260] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-63] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-133] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-155] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-156] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-161] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-186] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-204] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-186] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-263] for track '30' has 3 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.