# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_7`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [1-329] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [1-51] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-263] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-70] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [1-64] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-275] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-196] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-188] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-190] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-270] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-328] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-203] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-329] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [232-248] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-276] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-251] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-18] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-26] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-73] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-329] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-15] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-198] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-181] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-205] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-181] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-298] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-153] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [204-264] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-199] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-293] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-269] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-303] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-237] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.