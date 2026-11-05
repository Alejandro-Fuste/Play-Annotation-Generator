# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_16`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [112-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-200] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-462] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-530] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-358] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-390] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-206] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-218] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-367] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-473] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-477] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-324] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-381] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-569] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-202] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-241] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [244-393] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-417] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-406] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-332] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-345] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-403] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-348] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-469] for track '29' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.