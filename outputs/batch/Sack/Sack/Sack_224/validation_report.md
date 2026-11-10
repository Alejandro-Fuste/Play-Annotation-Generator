# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_224`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_224/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
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
> - Row 450: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [79-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [94-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [104-120] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [99-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-120] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-107] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-119] for track '23' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.