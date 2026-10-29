# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_109`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 219: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 220: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_PreSnap' range [0-201] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-268] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-266] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-264] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-207] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-230] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [150-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-244] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-254] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-199] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-246] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-252] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-154] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-261] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-252] for track '26' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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