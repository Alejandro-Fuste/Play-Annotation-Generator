# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_59`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 64: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_ScreenBlock' range [3-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-133] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-223] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-230] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-187] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-133] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-219] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-165] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-190] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-161] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-207] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-58] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-223] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-233] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-200] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-36] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-204] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-223] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-194] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-223] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-231] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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