# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_187`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_187/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 35 |
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
> - Action 'Action_SackQuarterback' range [113-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [113-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-55] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-95] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '23' has 1 frames without a visible bounding box.
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