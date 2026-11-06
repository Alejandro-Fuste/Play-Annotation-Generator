# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_34`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 38 |
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
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-206] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-196] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-206] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-210] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.