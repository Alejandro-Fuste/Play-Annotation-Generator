# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_92`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 399 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 185: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 186: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - Row 186: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 186: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
> - Action 'Action_None' range [299-369] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-337] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-399] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-377] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-393] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-399] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-337] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-369] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-399] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [332-383] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-319] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-319] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-346] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-371] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [302-334] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-369] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-394] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-318] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-360] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-399] for track '26' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.