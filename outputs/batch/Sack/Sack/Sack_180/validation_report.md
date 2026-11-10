# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_180`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_180/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_SackQuarterback' range [119-150] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [115-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [97-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [109-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-79] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-88] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-111] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '23' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.