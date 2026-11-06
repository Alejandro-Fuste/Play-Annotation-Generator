# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_10`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
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
> - Action 'Action_None' range [11-233] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-153] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-49] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-56] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-95] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [11-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-213] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-226] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-185] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-196] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-219] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-233] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.