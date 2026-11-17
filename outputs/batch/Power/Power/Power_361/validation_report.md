# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_361`
- **Input XML**: `outputs/batch/Power/Power/Power_361/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 722: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [19-243] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-249] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-269] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-268] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [154-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [163-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [202-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-26] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-225] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-233] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-220] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-215] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-249] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [154-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [183-206] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-218] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-163] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-171] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-242] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-254] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-269] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-33] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-233] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-240] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '25' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.