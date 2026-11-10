# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_151`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_151/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 36 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-48] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [129-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-79] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-84] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-119] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '18' has 1 frames without a visible bounding box.
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