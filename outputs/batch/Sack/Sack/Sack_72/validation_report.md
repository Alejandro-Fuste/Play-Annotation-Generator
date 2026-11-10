# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_72`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_72/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
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
> - Action 'Action_PreSnap' range [0-84] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [71-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [93-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-53] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-72] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-62] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-98] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-87] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-82] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [113-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-108] for track '19' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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