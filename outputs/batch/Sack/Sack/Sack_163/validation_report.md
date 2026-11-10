# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_163`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_163/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-26] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-93] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [66-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [80-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [107-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [111-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [114-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-82] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-109] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-25] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-28] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-74] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-82] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '19' has 1 frames without a visible bounding box.
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