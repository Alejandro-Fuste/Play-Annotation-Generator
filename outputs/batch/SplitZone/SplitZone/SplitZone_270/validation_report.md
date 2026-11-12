# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_270`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_270/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 542: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_SplitBlock' range [221-253] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [255-283] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-291] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [218-279] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-339] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [218-274] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-293] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [218-258] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-246] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [256-318] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [320-344] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [346-353] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-242] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-359] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-319] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-29] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-332] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-343] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-359] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-314] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-214] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-356] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [218-268] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-45] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-227] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-344] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-348] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-335] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-342] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-349] for track '26' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.