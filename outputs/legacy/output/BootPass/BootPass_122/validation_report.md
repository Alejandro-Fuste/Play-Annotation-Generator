# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_122`
- **Input XML**: `output/BootPass/BootPass_122/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 5 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 31 could not be resolved to any XML tracks (position/team_side missing).
> - Event 'Action_SecureCatch' at frame 173 targets track ID '72', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-167] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [133-141] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-183] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-110] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-13] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-20] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-30] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-44] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-189] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-203] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-196] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-199] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-203] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '31' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.