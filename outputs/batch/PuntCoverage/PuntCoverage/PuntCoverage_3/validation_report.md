# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_3`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 65 |
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
> - Action 'Action_PreSnap' range [0-54] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-263] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-71] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-262] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-220] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_Tackle' range [221-224] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [232-263] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-161] for track '13' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-259] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-104] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-156] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-245] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-45] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-128] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-269] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-112] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-243] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-269] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-190] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-207] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.