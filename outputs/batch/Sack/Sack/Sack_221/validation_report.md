# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_221`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_221/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
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
> - Action 'Action_PreSnap' range [0-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-120] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [90-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-45] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-52] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-88] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-77] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [60-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [78-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-62] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '23' has 1 frames without a visible bounding box.
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
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.