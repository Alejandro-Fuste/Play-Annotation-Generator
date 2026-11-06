# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_37`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 76: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 76: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [24-310] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-265] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-315] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-320] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-251] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-82] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-165] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-245] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-302] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-274] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-231] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-242] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [229-242] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-250] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-242] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-299] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-268] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-273] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-295] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-329] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-327] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-300] for track '39' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [302-305] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '41' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.