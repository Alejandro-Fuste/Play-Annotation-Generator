# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_31`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-71] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-29] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [83-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-23] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-39] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-55] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-46] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-90] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-69] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-90] for track '23' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.