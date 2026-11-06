# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_24`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-43] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-53] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-83] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-281] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-44] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-60] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-12] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [226-231] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-291] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [208-225] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [229-265] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [267-268] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [272-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-113] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-155] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-196] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-158] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-217] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-273] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-244] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-238] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.