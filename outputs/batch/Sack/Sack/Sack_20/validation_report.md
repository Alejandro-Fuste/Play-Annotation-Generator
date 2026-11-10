# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_20`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
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
> - Action 'Action_WrapQuarterback' range [105-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [117-118] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [120-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-161] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-137] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-142] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-180] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-180] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-130] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.