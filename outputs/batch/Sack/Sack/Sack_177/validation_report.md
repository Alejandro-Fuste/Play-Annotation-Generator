# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_177`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_177/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 40 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-48] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-49] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [50-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [78-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [85-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [50-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [82-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [88-89] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-90] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-28] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-90] for track '19' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.