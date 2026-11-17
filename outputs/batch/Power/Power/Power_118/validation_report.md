# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_118`
- **Input XML**: `outputs/batch/Power/Power/Power_118/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 238: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [3-359] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-275] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-288] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-317] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-256] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-293] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-337] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [238-246] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [251-253] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [238-282] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-258] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-348] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-331] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-346] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-292] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-318] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-355] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-294] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-293] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-353] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-297] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-262] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-248] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [238-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-281] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-340] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-338] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-64] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-128] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-214] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-283] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-147] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-292] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-347] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-343] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-341] for track '28' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.