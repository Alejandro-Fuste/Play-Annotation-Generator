# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_51`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 104: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [62-122] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-214] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-329] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [62-259] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-287] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-294] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-320] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-300] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [305-307] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-181] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-202] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-213] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-248] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-298] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-212] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-250] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-257] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-287] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-292] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-114] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-291] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-240] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-314] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-274] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [277-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '28' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.