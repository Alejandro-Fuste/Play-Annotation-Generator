# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_1`
- **Input XML**: `output_showcase_final/WRSlowScreens/WRSlowScreens_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 4: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 4: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_PassBlock' for track '22' has invalid range: start=22, end=19. Clamping end to start.
> - Action 'Action_RunAfterCatch' range [110-218] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [220-241] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-236] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-51] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-231] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-224] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [19-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-262] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-117] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [173-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-179] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [55-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [128-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-15] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-50] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-130] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' for track '22' starts at frame 19, but the player has no visible bounding box on this frame.
> - Action 'Action_BallSnap' range [19-19] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-30] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-59] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [72-78] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-88] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-88] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-216] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-254] for track '40' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.