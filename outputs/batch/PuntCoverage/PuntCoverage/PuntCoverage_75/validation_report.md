# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_75`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 45 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_BallCarry' for track '24' has invalid range: start=234, end=232. Clamping end to start.
> - Action 'Action_PreSnap' range [0-252] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-145] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-154] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-168] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-59] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-232] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-238] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-258] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '28' has 1 frames without a visible bounding box.
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