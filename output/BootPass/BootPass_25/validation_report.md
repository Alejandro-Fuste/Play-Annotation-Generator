# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_25`
- **Input XML**: `output/BootPass/BootPass_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 49 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-216] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-224] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-308] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-302] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-319] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-327] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-327] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-327] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-328] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-309] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-316] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-159] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-301] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-101] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-148] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-316] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-319] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-329] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-101] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-101] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-101] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-287] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-85] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-99] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-299] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-326] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-277] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-283] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-301] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-327] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-248] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-279] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-297] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-313] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-323] for track '31' has 1 frames without a visible bounding box.
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