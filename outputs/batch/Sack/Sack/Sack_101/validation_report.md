# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_101`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_101/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 50 |
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
> - Action 'Action_PreSnap' range [0-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-120] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-120] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [108-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-101] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-62] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-119] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-106] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '25' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.