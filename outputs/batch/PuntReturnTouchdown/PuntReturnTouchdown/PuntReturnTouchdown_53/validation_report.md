# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_53`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 107: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [58-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-154] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-186] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-389] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-207] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-311] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-287] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-389] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-389] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-155] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-187] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [58-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [81-87] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [90-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [95-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-368] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-383] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-75] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [205-253] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-279] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [282-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-195] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-211] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-273] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-197] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-376] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-316] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-365] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-377] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [380-389] for track '32' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.