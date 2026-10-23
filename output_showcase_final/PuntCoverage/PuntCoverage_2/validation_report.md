# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_2`
- **Input XML**: `output_showcase_final/PuntCoverage/PuntCoverage_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 6: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [4-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-96] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-89] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-111] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-176] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-145] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-158] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-90] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-72] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-158] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-131] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-209] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-218] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-102] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-154] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-229] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-132] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-175] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-229] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '31' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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