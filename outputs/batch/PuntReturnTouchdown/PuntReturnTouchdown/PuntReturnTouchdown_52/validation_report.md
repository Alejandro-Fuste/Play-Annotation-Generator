# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_52`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 105: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - Row 106: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [20-299] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [71-295] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-277] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-218] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-253] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-284] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-259] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-289] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.