# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_50`
- **Input XML**: `output/BootPass/BootPass_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 33 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-214] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-212] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-103] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-92] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-86] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-95] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-117] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-172] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-49] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-95] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-149] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-92] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-217] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-197] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-239] for track '35' has 1 frames without a visible bounding box.
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