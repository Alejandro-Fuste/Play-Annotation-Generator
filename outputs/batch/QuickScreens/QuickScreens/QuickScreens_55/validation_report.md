# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_55`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 60: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [8-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [76-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [156-171] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [173-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [178-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [188-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-177] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-191] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-224] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-98] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [8-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-175] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [8-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-183] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-239] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [8-200] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-238] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-200] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-225] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-61] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-53] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-185] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [8-17] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-35] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-78] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-100] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-146] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-198] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '30' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.