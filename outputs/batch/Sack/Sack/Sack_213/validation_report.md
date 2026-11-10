# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_213`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_213/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-136] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-195] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [106-168] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-169] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-183] for track '10' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-196] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-23] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-72] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-166] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-159] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-232] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-329] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-174] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-187] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-204] for track '21' has 1 frames without a visible bounding box.
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
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.