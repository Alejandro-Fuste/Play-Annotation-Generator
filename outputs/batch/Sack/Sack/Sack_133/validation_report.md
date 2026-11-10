# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_133`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_133/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 35 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-24] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-95] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [60-66] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [81-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [117-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-98] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [94-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [103-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '18' has 1 frames without a visible bounding box.
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