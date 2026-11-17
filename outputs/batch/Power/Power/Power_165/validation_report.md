# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_165`
- **Input XML**: `outputs/batch/Power/Power/Power_165/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 332: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 332: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 332: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-198] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-208] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-216] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-323] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-320] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-228] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-319] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-224] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-237] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [148-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-237] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-263] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-278] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-300] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-303] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-326] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-217] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-303] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-318] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-296] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-321] for track '30' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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