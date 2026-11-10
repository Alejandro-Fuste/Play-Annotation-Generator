# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_36`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 38 |
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
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [109-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-121] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-131] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [97-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '23' has 1 frames without a visible bounding box.
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