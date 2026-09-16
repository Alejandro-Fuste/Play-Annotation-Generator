# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_96`
- **Input XML**: `output/BootPass/BootPass_96/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 53 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '9' has invalid range: start=213, end=87. Clamping end to start.
> - Action 'Action_PreSnap' range [0-86] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-125] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 101, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [101-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-103] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-53] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-130] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-128] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-126] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-140] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-170] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-139] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-152] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-269] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-224] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-167] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-164] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-269] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-195] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-269] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-205] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-264] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-237] for track '40' has 1 frames without a visible bounding box.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.