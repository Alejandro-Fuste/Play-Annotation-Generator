# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_46`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
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
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [113-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [123-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [143-150] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-26] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-29] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-150] for track '19' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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