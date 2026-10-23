# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_64`
- **Input XML**: `output/BootPass/BootPass_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 35 |
| Ball Tracks | 2 |
| CSV events parsed | 7 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 40 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-224] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-110] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-111] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-137] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-197] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-87] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-178] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-125] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-86] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-161] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-184] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-216] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-132] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-140] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-152] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-199] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-227] for track '33' has 2 frames without a visible bounding box.
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
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
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