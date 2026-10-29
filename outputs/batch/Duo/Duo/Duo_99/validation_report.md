# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_99`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 199: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 199: Duplicate assignment for track ID '22' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Action 'Action_PreSnap' range [0-249] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-280] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-305] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-220] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-315] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-358] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-207] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-318] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-358] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-279] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-257] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-315] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-358] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-252] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-310] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-358] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [197-222] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-271] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-304] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-32] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-258] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-244] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-248] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-254] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-266] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-309] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-276] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-281] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-289] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-313] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-323] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-327] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-339] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-346] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-346] for track '29' has 2 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.