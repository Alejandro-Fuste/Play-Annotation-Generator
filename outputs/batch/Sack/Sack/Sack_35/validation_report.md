# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_35`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 43 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [113-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [151-157] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [160-165] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [91-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-132] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-180] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [124-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-110] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-149] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-174] for track '27' has 3 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.