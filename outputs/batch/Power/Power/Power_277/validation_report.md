# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_277`
- **Input XML**: `outputs/batch/Power/Power/Power_277/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 554: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 554: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 554: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 554: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-262] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-229] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-277] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [166-225] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [166-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [184-207] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [166-188] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [205-225] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-260] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-271] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.