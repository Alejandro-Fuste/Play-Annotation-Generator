# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_141`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_141/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 33 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-120] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [54-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [85-96] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [105-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-120] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-73] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-119] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '20' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.