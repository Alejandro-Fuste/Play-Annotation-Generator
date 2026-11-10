# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_179`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_179/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 16 |
| Player Tracks | 16 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
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
> - Action 'Action_PreSnap' range [0-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [119-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [130-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [89-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [121-122] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [135-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-105] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-126] for track '15' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.