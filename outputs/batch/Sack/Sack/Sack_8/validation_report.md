# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_8`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 31 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_WrapQuarterback' for track '14' has invalid range: start=67, end=63. Clamping end to start.
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-88] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-58] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-36] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [51-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [62-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [79-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '18' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.