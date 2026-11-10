# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_40`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 37 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-66] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-97] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-78] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [89-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [79-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [90-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [94-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [123-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [118-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-150] for track '19' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.