# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_14`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_14/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 17 |
| Player Tracks | 17 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 32 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' for track '4' starts at frame 120, but the player has no visible bounding box on this frame.
> - Action 'Action_SackQuarterback' range [120-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-120] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [115-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-94] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-119] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-12] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-18] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-113] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '16' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.