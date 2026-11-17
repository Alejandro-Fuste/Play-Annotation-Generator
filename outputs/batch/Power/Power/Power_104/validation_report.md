# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_104`
- **Input XML**: `outputs/batch/Power/Power/Power_104/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 210: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-32] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-63] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-67] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-103] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-147] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-237] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-244] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-249] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [164-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-232] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-294] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-298] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [164-168] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [170-184] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [245-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-257] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-245] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-279] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [164-215] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [237-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-237] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-182] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-232] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-78] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-171] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-255] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-272] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-205] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-269] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-294] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-219] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-188] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-202] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-212] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-278] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-298] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-294] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-283] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-299] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-295] for track '27' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.