# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_222`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_222/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [6-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-120] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [96-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [116-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-99] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-105] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-74] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-120] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-71] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-120] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-57] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [69-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-90] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-35] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-120] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-90] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-92] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-120] for track '27' has 1 frames without a visible bounding box.
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