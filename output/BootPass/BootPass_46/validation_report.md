# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_46`
- **Input XML**: `output/BootPass/BootPass_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 30 |
| Ball Tracks | 1 |
| CSV events parsed | 6 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 94 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-165] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '20' starts at frame 95, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [95-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [121-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-130] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_RunFlatRoute' range [150-153] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-239] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '29' has 1 frames without a visible bounding box.
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