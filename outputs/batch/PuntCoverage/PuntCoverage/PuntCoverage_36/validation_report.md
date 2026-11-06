# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_36`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [15-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-219] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [170-199] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-208] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-203] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-163] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-193] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-82] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-213] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-228] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-234] for track '29' has 2 frames without a visible bounding box.
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