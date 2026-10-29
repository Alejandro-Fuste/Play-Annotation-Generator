# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_41`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 84: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 84: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - Row 84: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 84: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_PreSnap' range [0-231] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-250] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [127-224] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-204] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [127-170] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [174-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [193-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [199-218] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-242] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [127-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-268] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-235] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-240] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-256] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-268] for track '26' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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