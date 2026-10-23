# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_85`
- **Input XML**: `output/BootPass/BootPass_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 6 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 114 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-232] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-257] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-359] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-306] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-350] for track '3' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-356] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-286] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-230] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-291] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-314] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-326] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-333] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-281] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-291] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-324] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-341] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-356] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-152] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-270] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-286] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-296] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-359] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-308] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-355] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-231] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-334] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-342] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-359] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.