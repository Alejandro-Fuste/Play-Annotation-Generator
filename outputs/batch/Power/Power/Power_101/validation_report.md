# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_101`
- **Input XML**: `outputs/batch/Power/Power/Power_101/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 204: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-204] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-226] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-250] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-145] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-241] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-172] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-289] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-203] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-171] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-217] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-252] for track '18' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-297] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [108-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-174] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-190] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-224] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-299] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-265] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-294] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.