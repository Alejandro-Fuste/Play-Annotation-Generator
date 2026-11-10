# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_161`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_161/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 15 |
| Player Tracks | 15 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 29 |
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
> - Action 'Action_PreSnap' range [0-22] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [116-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [123-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [139-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-132] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-23] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [103-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [129-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '14' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.