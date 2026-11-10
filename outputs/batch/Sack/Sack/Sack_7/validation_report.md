# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_7`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-147] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-163] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-178] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-26] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-42] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-88] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-147] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-179] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [106-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [131-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [134-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [150-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [172-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-179] for track '20' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-173] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-180] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.