# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_112`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_112/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 226: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-171] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-180] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-88] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-95] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-110] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [124-148] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [150-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [103-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-143] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-180] for track '21' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.