# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_27`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 64 |
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
> - Action 'Action_PreSnap' range [0-53] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [209-281] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-202] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-123] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-299] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-211] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-255] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-42] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-8] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-23] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-265] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-297] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-278] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-292] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-294] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-279] for track '30' has 1 frames without a visible bounding box.
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