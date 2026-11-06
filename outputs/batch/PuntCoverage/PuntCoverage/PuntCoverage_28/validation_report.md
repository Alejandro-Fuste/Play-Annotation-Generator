# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_28`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_28/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 57: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [13-263] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [13-51] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [60-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [67-68] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [70-71] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-225] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-237] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-284] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-293] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-227] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-297] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-74] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-184] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-279] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-292] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [231-251] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [254-289] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-234] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-167] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-281] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-298] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-279] for track '28' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.