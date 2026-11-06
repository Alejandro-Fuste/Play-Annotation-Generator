# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_30`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_PuntBall' for track '18' has invalid range: start=66, end=39. Clamping end to start.
> - Action 'Action_None' range [9-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-89] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-266] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-170] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-252] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-268] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-246] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-231] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-208] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-207] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-36] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-234] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-187] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-244] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-267] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [185-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [226-233] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-244] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [251-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [256-267] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-222] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-228] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-252] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '30' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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